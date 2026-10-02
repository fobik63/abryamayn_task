"""Запуск: python run_mission.py --days 6 --seed 42"""
import argparse
import csv
import sched
import time
from mission import delta_v, flight_time, fuel_needed, random_event


def build_parser():
    p = argparse.ArgumentParser(description="Симулятор межпланетной миссии")
    p.add_argument("--days",  type=int,   default=5,    help="длительность миссии, сут")
    p.add_argument("--seed",  type=int,   default=None, help="зерно ГСЧ")
    p.add_argument("--speed", type=float, default=0.2,  help="секунда на 1 сутки")
    p.add_argument("--csv",   type=str,   default=None, help="сохранить отчёт в CSV")
    return p


def main():
    args = build_parser().parse_args()
    resource = 100
    s = sched.scheduler(time.time, time.sleep)
    log = []

    m0 = 45000
    m1 = 20000
    isp = 300
    dv = delta_v(m0, m1, isp)
    fuel = fuel_needed(m1, 3000, isp)
    ft = flight_time(78_000_000, 0.001)

    print("=== Расчёты миссии ===")
    print(f"Δv ({m0} → {m1} кг, Isp={isp}): {dv:.1f} м/с")
    print(f"Топливо для Δv=3000 м/с: {fuel:.0f} кг")
    print(f"Время перелёта (78 000 000 км, a=0.001 км/с²): {ft:.1f} ч")
    print()

    def day_report(day):
        nonlocal resource
        desc, delta = random_event(args.seed + day if args.seed is not None else None)
        resource = max(0, min(100, resource + delta))
        bar = "#" * (resource // 5)
        line = f"Сутки {day:>2} | {desc:<38s} [delta:{delta:+3d} | ресурс {resource:3d}]% {bar}"
        print(line)
        log.append((day, desc, delta, resource))
        if resource == 0:
            for ev in list(s.queue):
                s.cancel(ev)
            return
        if day < args.days:
            s.enter(args.speed, 1, day_report, (day + 1,))

    s.enter(0, 1, day_report, (1,))
    start_time = time.time()
    s.run()
    elapsed = time.time() - start_time

    print(f"\nМиссия завершена. Итоговый ресурс: {resource}%. "
          f"Общее время симуляции: {elapsed:.1f} с")

    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["day", "event", "delta", "resource"])
            for row in log:
                writer.writerow(row)
        print(f"Отчёт сохранён в {args.csv}")


if __name__ == "__main__":
    main()