from datetime import datetime

import matplotlib.pyplot as plt
from openpyxl import load_workbook

dates = []
daily_energy = []

workbook = load_workbook("solar_data.xlsx", read_only=True)
try:
    sheet = workbook.active

    for date, power_kw, hours in sheet.iter_rows(
        min_row=2, max_col=3, values_only=True
    ):
        if date is None and power_kw is None and hours is None:
            continue

        if isinstance(date, datetime):
            date = date.strftime("%Y-%m-%d")

        if power_kw is None or hours is None:
            print(f"{date} 缺少功率或运行时长，已跳过")
            continue

        energy = float(power_kw) * float(hours)
        dates.append(str(date))
        daily_energy.append(energy)
        print(f"{date} 发电量：{energy:.1f} kWh")
finally:
    workbook.close()

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
    plt.savefig("solar_trend_excel.png", dpi=150)
    plt.close()
    print("趋势图已保存到 solar_trend_excel.png")