# 光伏发电数据分析

这个 Python 项目读取 CSV 或 Excel 格式的光伏运行记录，计算每日发电量，并生成趋势图。

## 数据说明

项目中有两份内容相同的样例数据：`solar_data.csv` 和 `solar_data.xlsx`。

| 列名 | 含义 | 单位 |
|---|---|---|
| `date` | 记录日期 | 年-月-日 |
| `power_kw` | 平均功率 | 千瓦（kW） |
| `hours` | 运行时长 | 小时（h） |

每日发电量（kWh）= 平均功率（kW）× 运行时长（h）。功率或时长为空时，程序会提示并跳过该记录。日均发电量只按有效天数计算。

## 运行方法

在 VS Code 中打开 `solar_analysis` 文件夹，然后打开终端（Terminal）。首次运行时，依次执行以下命令创建虚拟环境（Virtual Environment）并安装依赖（Dependencies）。

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install matplotlib openpyxl
```

根据数据格式运行对应的脚本（Script）。

```powershell
# 读取 CSV，生成 solar_trend.png
.\.venv\Scripts\python.exe read_data.py

# 读取 Excel，生成 solar_trend_excel.png
.\.venv\Scripts\python.exe read_excel.py
```

## 样例结果

| 日期 | 发电量 |
|---|---:|
| 2026-11-01 | 200.0 kWh |
| 2026-11-02 | 240.0 kWh |
| 2026-11-03 | 135.0 kWh |
| 2026-11-04 | 功率缺失，已跳过 |

两种数据格式的统计结果一致。有效天数为 **3 天**，总发电量为 **575.0 kWh**，日均发电量为 **191.7 kWh**。生成的 PNG 趋势图保存在项目文件夹里。