import mcp3021_driver as mcp
import adc_plot as plot
import time

MCP = mcp.MCP3021(5.2)
voltages = []
times = []
duration = 3.0

try:
    start_time = time.time()
    while (time.time() - start_time < duration):
        value = MCP.get_voltage()
        current_time = time.time() - start_time

        voltages.append(value)
        times.append(current_time)
        
    plot.plot_voltage_vs_time(times, voltages, MCP.dynamic_range*1.1)
    plot.plot_sampling_period_hist(times)
finally:
    MCP.deinit()