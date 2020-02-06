#!/usr/bin/env python3
import yaml
import matplotlib
# matplotlib.use("Agg")
from matplotlib.patches import Circle, Rectangle, Arrow
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import matplotlib.animation as manimation
import argparse
import math
import copy

Colors = ['green']#, 'blue', 'green']


class Animation:
  def __init__(self, map, schedule):
    self.map = map
    self.schedule = schedule

    aspect = map["map"]["dimensions"][0] / map["map"]["dimensions"][1]

    self.fig = plt.figure(frameon=False, figsize=(8 * aspect, 8))
    self.ax = self.fig.add_subplot(111, aspect='equal')
    self.fig.subplots_adjust(left=0,right=1,bottom=0,top=1, wspace=None, hspace=None)
    # self.ax.set_frame_on(False)

    self.patches = []
    self.artists = []
    self.patches2 = []
    self.artists2 = []
    self.agents = dict()
    self.agent_names = dict()
    # create boundary patch
    xmin = -0.5
    ymin = -0.5
    xmax = map["map"]["dimensions"][0] - 0.5
    ymax = map["map"]["dimensions"][1] - 0.5

    # self.ax.relim()
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    # self.ax.set_xticks([])
    # self.ax.set_yticks([])
    # plt.axis('off')
    # self.ax.axis('tight')
    # self.ax.axis('off')

    self.patches.append(Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, facecolor='none', edgecolor='none'))
    for o in map["map"]["obstacles"]:
      x, y = o[0], o[1]
      self.patches.append(Rectangle((x - 0.5, y - 0.5), 1, 1, facecolor='black', edgecolor='black'))

    # create agents:
    self.T = 0
    agent_seg = True
    # draw goals first
    for d, i in zip(map["agents"], range(0, len(map["agents"]))):
      self.patches.append(Rectangle((d["goal"][0] - 0.25, d["goal"][1] - 0.25), 0.5, 0.5, facecolor=Colors[i%len(Colors)], edgecolor='black', alpha=0.5))
    for d, i in zip(map["agents"], range(0, len(map["agents"]))):
      name = d["name"]
      if agent_seg:
        if self.agentSeg(d["start"], d["goal"]):
          self.agents[name] = Circle((d["start"][0], d["start"][1]), 0.3, facecolor=Colors[i%len(Colors)], edgecolor='black')
          self.agents[name].original_face_color = Colors[i%len(Colors)]
        else:
          self.agents[name] = Circle((d["start"][0], d["start"][1]), 0.3, facecolor='orange', edgecolor='black')
          self.agents[name].original_face_color = 'orange'
      else:
        self.agents[name] = Circle((d["start"][0], d["start"][1]), 0.3, facecolor=Colors[i%len(Colors)], edgecolor='black')
        self.agents[name].original_face_color = Colors[i%len(Colors)]
      self.patches.append(self.agents[name])
      self.T = max(self.T, schedule["schedule"][name][-1]["t"])
      self.agent_names[name] = self.ax.text(d["start"][0], d["start"][1], "")# name.replace('agent', ''))
      self.agent_names[name].set_horizontalalignment('center')
      self.agent_names[name].set_verticalalignment('center')
      self.artists.append(self.agent_names[name])


    # self.ax.set_axis_off()
    # self.fig.axes[0].set_visible(False)
    # self.fig.axes.get_yaxis().set_visible(False)

    # self.fig.tight_layout()

    self.anim = animation.FuncAnimation(self.fig, self.animate_func,
                               init_func=self.init_func,
                               # frames=int(self.T+1) * 10,
                               frames=1,
                               interval=100,
                               blit=True)
    # self.ax2 = self.fig.add_subplot(122, aspect='equal')
    # draw goals first

  def save(self, file_name, speed):
    self.anim.save(
      file_name,
      "ffmpeg",
      fps=10 * speed,
      dpi=200),
      # savefig_kwargs={"pad_inches": 0, "bbox_inches": "tight"})

  def show(self):
    plt.show()

  def init_func(self):
    self.drawHWY("shared")
    self.drawHWY("longest")
    # self.drawPaths()
    for p in self.patches:
      self.ax.add_patch(p)
    for a in self.artists:
      self.ax.add_artist(a)
    self.drawPaths()
    return self.patches + self.artists

  def animate_func(self, i):
    for agent_name in self.schedule["schedule"]:
      agent = schedule["schedule"][agent_name]
      pos = self.getState(i / 10, agent)
      p = (pos[0], pos[1])
      self.agents[agent_name].center = p
      self.agent_names[agent_name].set_position(p)

    # reset all colors
    for _,agent in self.agents.items():
      agent.set_facecolor(agent.original_face_color)

    # check drive-drive collisions
    agents_array = [agent for _,agent in self.agents.items()]
    for i in range(0, len(agents_array)):
      for j in range(i+1, len(agents_array)):
        d1 = agents_array[i]
        d2 = agents_array[j]
        pos1 = np.array(d1.center)
        pos2 = np.array(d2.center)
        if np.linalg.norm(pos1 - pos2) < 0.7:
          d1.set_facecolor('red')
          d2.set_facecolor('red')
          print("COLLISION! (agent-agent) ({}, {})".format(i, j))
    plt.waitforbuttonpress()
    return self.patches + self.artists


  def getState(self, t, d):
    idx = 0
    while idx < len(d) and d[idx]["t"] < t:
      idx += 1
    if idx == 0:
      return np.array([float(d[0]["x"]), float(d[0]["y"])])
    elif idx < len(d):
      posLast = np.array([float(d[idx-1]["x"]), float(d[idx-1]["y"])])
      posNext = np.array([float(d[idx]["x"]), float(d[idx]["y"])])
    else:
      return np.array([float(d[-1]["x"]), float(d[-1]["y"])])
    dt = d[idx]["t"] - d[idx-1]["t"]
    t = (t - d[idx-1]["t"]) / dt
    pos = (posNext - posLast) * t + posLast
    return pos

  def drawPaths(self):
    for agent_name in self.schedule["schedule"]:
      agent = self.schedule["schedule"][agent_name]
      path = np.zeros((len(agent), 2))
      for i in range(len(agent)):
        path[i, 0] = agent[i]["x"]
        path[i, 1] = agent[i]["y"]
      self.ax.plot(path[:,0], path[:,1])

  def drawHWY(self, heuristic="longest"):
    max_t = 0
    hwy_agent = None
    hwy_name = "agent0"
    if heuristic == "longest":
      for agent_name in self.schedule["schedule"]:
        agent = self.schedule["schedule"][agent_name]
        if max_t < len(agent):
          max_t = len(agent)
          hwy_name = agent_name
      hwy = np.zeros((max_t, 2))
      hwy_agent = self.schedule["schedule"][hwy_name]
      for i in range(max_t):
        hwy[i, 0] = hwy_agent[i]["x"]
        hwy[i, 1] = hwy_agent[i]["y"]
      self.ax.plot(hwy[:,0], hwy[:,1], color='red', linewidth=8)
    if heuristic == "shared":
      dim_x = self.map["map"]["dimensions"][0]
      dim_y = self.map["map"]["dimensions"][1]
      hwy_array = np.zeros((dim_x, dim_y))
      for agent_name in self.schedule["schedule"]:
        agent = self.schedule["schedule"][agent_name]
        for i in range(len(agent)):
          col = agent[i]["y"]
          row = agent[i]["x"]
          hwy_array[col, row] = hwy_array[col, row] + 1
      thresh = max(2, int(0.3 * np.amax(hwy_array)))
      hwy_array[hwy_array < thresh] = 0
      ind_y, ind_x = np.where(hwy_array > 0)
      for x, y in zip(ind_x, ind_y):
        self.patches.append(Rectangle((x - 0.5, y - 0.5), 1, 1, facecolor='red', edgecolor='red', alpha=0.2))

  def agentSeg(self, start, goal):
    x = self.map["map"]["dimensions"][0]
    y = self.map["map"]["dimensions"][1]
    thresh = (x*x/4)+(y*y/4)
    dist = (start[0] - goal[0])*(start[0] - goal[0]) +  (start[1] - goal[1])*(start[1] - goal[1])
    if dist < thresh:
      # print("local")
      return True
    else:
      # print("global")
      return False

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("map", help="input file containing map")
  parser.add_argument("schedule", help="schedule for agents")
  parser.add_argument('--video', dest='video', default=None, help="output video file (or leave empty to show on screen)")
  parser.add_argument("--speed", type=int, default=1, help="speedup-factor")
  args = parser.parse_args()


  with open(args.map) as map_file:
    map = yaml.load(map_file, Loader=yaml.FullLoader)

  with open(args.schedule) as states_file:
    schedule = yaml.load(states_file, Loader=yaml.FullLoader)

  animation = Animation(map, schedule)
  if args.video:
    animation.save(args.video, args.speed)
  else:
    animation.show()
    # animation2.show()
    # plt.waitforbuttonpress(0)

