def check_current_rate(time_hour):

    # เรทค่าไฟราคาถูก (Off-peak) เริ่มหลัง 21:00 น. ไปจนถึง 06:00 น.
    if time_hour >= 21 or time_hour <= 6:
        return "CHEAP"
    else:
        return "EXPENSIVE"
    