import sched

tick = 0

def fake_time():
    return tick

def fake_sleep(delay):
    global tick
    tick += delay

s = sched.scheduler(fake_time, fake_sleep)

def say(text):
    print(f"[t={tick:.1f}] {text}")

s.enter(2, 1, say, ("Прошло 2 секунды (приоритет 1)",))
s.enter(2, 0, say, ("Прошло 2 секунды (приоритет 0 — сработает ПЕРВЫМ)",))
s.enter(1, 1, say, ("Прошла 1 секунда",))
s.enter(3, 1, say, ("Абсолютное время t=3",))
s.enter(0.5, 1, say, ("Прошло 0.5 секунды",))

print("Очередь до run():", len(s.queue), "задач")
print("Запуск в виртуальном времени:\n")

s.run()

print("\nГотово. Пустая очередь?", s.empty())
print("Финальное время:", tick)