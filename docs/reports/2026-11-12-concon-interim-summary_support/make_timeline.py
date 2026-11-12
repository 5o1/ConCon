"""Generate the timeline SVG for the ConCon interim summary.

Each event is (lane, date, label). Dates come from git logs and report dates
recorded in the review file (A2, A4, A7). Run: python3 make_timeline.py > timeline.svg
"""
from datetime import date

LANES = ["游戏线", "手柄物理资产", "固定手柄与可达性", "工作台与采集平台", "重定向", "真机与标定", "IK 自动驾驶"]
EVENTS = [
    (0, "2026-10-05", "贪吃蛇 RL 阶段一"), (0, "2026-10-29", "通关 172/200"),
    (1, "2026-10-06", "资产仓库首批提交"), (1, "2026-10-15", "v0.3.0 SDF"), (1, "2026-10-22", "v0.4.1"),
    (1, "2026-11-05", "摇杆按下 7.4 N"), (1, "2026-11-07", "v0.4.2 定制 SAPIEN"), (1, "2026-11-10", "v0.4.3"),
    (2, "2026-10-14", "改为先固定手柄"), (2, "2026-10-21", "方向键 IK/PPO"), (2, "2026-10-22", "双手可行性 K0"),
    (2, "2026-11-04", "任务 Z / demogen"),
    (3, "2026-10-16", "孪生 v4"), (3, "2026-10-20", "相机标定"), (3, "2026-10-22", "遥操采集平台"),
    (3, "2026-11-04", "支架 v3"), (3, "2026-11-09", "支架 v3.3"), (3, "2026-11-11", "厂商工作台"),
    (4, "2026-11-04", "左拇指解码"), (4, "2026-11-09", "解剖重定向 A–D"), (4, "2026-11-11", "调研"),
    (5, "2026-10-16", "确认无急停"), (5, "2026-11-11", "型号读取"), (5, "2026-11-12", "真机→仿真标定"),
    (6, "2026-11-11", "可行性调研"), (6, "2026-11-12", "13 任务实时运行"),
]
D0, D1 = date(2026, 10, 1), date(2026, 11, 14)
W, LEFT, TOP, LANE_H = 1040, 150, 40, 58
span = (D1 - D0).days
def x(d): return LEFT + (date.fromisoformat(d) - D0).days / span * (W - LEFT - 20)
H = TOP + LANE_H * len(LANES) + 40
out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="ConCon 时间线">',
       '<style>text{font-family:"Noto Sans CJK SC","Microsoft YaHei",sans-serif;fill:#182638}.l{font-size:14px;font-weight:600}.e{font-size:11.5px}.t{font-size:12px;fill:#546477}</style>']
for d in ["2026-10-01", "2026-10-08", "2026-10-15", "2026-10-22", "2026-10-29", "2026-11-05", "2026-11-12"]:
    out.append(f'<line x1="{x(d):.1f}" y1="{TOP-10}" x2="{x(d):.1f}" y2="{H-30}" stroke="#d9e3ea"/>')
    out.append(f'<text class="t" x="{x(d):.1f}" y="{H-12}" text-anchor="middle">{d[5:]}</text>')
for i, name in enumerate(LANES):
    y = TOP + i * LANE_H + LANE_H / 2
    out.append(f'<text class="l" x="10" y="{y+5:.1f}">{name}</text>')
    out.append(f'<line x1="{LEFT}" y1="{y:.1f}" x2="{W-20}" y2="{y:.1f}" stroke="#9fb3c2" stroke-dasharray="3 4"/>')
    evs = [e for e in EVENTS if e[0] == i]
    for k, (_, d, label) in enumerate(evs):
        dy = -10 if k % 2 == 0 else 20
        out.append(f'<circle cx="{x(d):.1f}" cy="{y:.1f}" r="5" fill="#155e75"/>')
        out.append(f'<text class="e" x="{x(d):.1f}" y="{y+dy:.1f}" text-anchor="middle">{label}</text>')
out.append('</svg>')
print("\n".join(out))
