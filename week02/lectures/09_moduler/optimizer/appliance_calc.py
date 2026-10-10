def should_turn_on(appliance_name, rate_status):
    
    # รายชื่อเครื่องใช้ไฟฟ้าที่กินไฟดุเดือด
    heavy_appliances = ["Dishwasher", "Renault Zoe Charger"]
    
    # ถ้าของกินไฟเยอะมาเจอช่วงค่าไฟแพง ให้สั่งหยุด
    if appliance_name in heavy_appliances and rate_status == "EXPENSIVE":
        return f"Do NOT start the {appliance_name} now. Wait until 21:00!"
    else:
        # ถ้าเป็นของชิ้นเล็ก หรืออยู่ในช่วงค่าไฟถูก ก็เปิดได้เลย
        return f"You can start the {appliance_name}."