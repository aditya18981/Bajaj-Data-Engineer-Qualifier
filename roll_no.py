path = "C:\Users\S41930\Downloads\Data Engineering\Data Engineering\data - sample"
def run(path) :     
    # import modules here 
    import pandas as pd 
    
    # logic 
    df = pd.read_excel(path)
    attendance_df =  pd.read_excel(df, sheet_name="attendance_data")
    attendance_df["attendance_date"] = pd.to_datetime(attendance_df["attendance_date"])
    absent_df = attendance_df[attendance_df["status"] == "Absent"].sort_values(["student_id", "attendance_date"])

    absence_streaks = []

    for student_id, group in absent_df.groupby("student_id"):
            dates = sorted(group["attendance_date"].tolist())
            
            if not dates:
                continue  
    
    streak_start = dates[0]
    prev_date = dates[0]
    
         
    


    
    
    # return your output
    return df