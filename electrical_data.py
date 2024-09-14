# Data from the image (Meter Reading and KWH/Day)
class electrical:
    
    def __init__(self,data) -> None:
        self.data
        
         
    meter_readings = [
        7399.7, 7410.2, 7420.2, 7430.6, 7441.2, 
        7452.0, 7463.1, 7473.5, 7484.6, 7495.3, 
        7505.8, 7516.8
    ]

    # Constant for scaling meter reading
    scale_factor = 320

    # Calculate daily KWH usage
    kwh_per_day = []
    for i in range(1, len(meter_readings)):
        daily_usage = (meter_readings[i] - meter_readings[i-1]) * scale_factor
        kwh_per_day.append(daily_usage)

    # Display results
    for day, kwh in enumerate(kwh_per_day, start=1):
        print(f"Day {day}: {kwh:.2f} KWH")