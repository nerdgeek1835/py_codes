def hour():
    hour = int (input('how much did you work today? '))
    while hour >12:
        print ('you are working too much')
        hour = int(input('how much did you work today? '))
    while  hour <= 12 and hour > 8:
        fee_hour = hour - (hour % 8) 
        overtime_hour = (hour % 8) * 1.5
        sum_hour = overtime_hour + fee_hour
        print('your salary will be calculated by fee hour + (overtime hour*1.5) which is: ' , sum_hour)
        return sum_hour
    while hour <= 8 :
        fee_hour = hour
        overtime_hour = 0
        sum_hour = overtime_hour + fee_hour
        print('your salary will be calculated by fee hour + (overtime hour*1.5) which is: ' , sum_hour)
        return sum_hour

def job_role():
    job_role = input('what is your job role? "worker" or "engineer"? ')
    engineer = 'engineer'
    worker = 'worker' 
    while job_role == engineer:
        print('nice, you are an engineer, your salary fee per hour will be: 90 ')
        engineer_fee_per_hour = 90
        return engineer_fee_per_hour
    while job_role == worker:
        print('nice, you are a worker, your salary fee per hour will be: 60 ')
        worker_fee_per_hour = 60
        return worker_fee_per_hour
    while job_role != engineer or worker:
        print('job is not defined')
        job_role = input('what is your job role? "worker" or "engineer" ? ')  
  
def hoghough(sum_hour , fee_per_hour):
    hoghough = sum_hour * fee_per_hour
    print (hoghough)

def main():
    while 1==1:        
        sum_hour = hour()
        fee_per_hour = job_role()
        hoghough(sum_hour , fee_per_hour)

main()
