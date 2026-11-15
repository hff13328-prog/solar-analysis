import csv

import matplotlib.pyplot as plt

dates = []
daily_energy = []

with open("solar_data.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        date = row["date"]
        power_text = row["power_kw"].strip()
        hours_text = row["hours"].strip()

        if power_text == "" or hours_text == "":
            print(f"{date} 缺少功率或运行时长，已跳过")
            continue

        power = float(power_text)
        hours = float(hours_text)
        energy = power * hours

        dates.append(date)
        daily_energy.append(energy)
        print(f"{date} 发电量：{energy:.1f} kWh")

valid_days = len(daily_energy)
total_energy = sum(daily_energy)

print()
print(f"有效天数：{valid_days} 天")
print(f"总发电量：{total_energy:.1f} kWh")

if valid_days > 0:
    average_energy = total_energy / valid_days
    print(f"日均发电量：{average_energy:.1f} kWh")

    plt.plot(dates, daily_energy, marker="o")
    plt.title("Daily Solar Energy")
    plt.xlabel("Date")
    plt.ylabel("Energy (kWh)")
    plt.ylim(bottom=0)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig("solar_trend.png", dpi=150)
    plt.close()
    print("趋势图已保存到 solar_trend.png")