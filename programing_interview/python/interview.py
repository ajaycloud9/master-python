"""
Write a function canAttendMeetings that takes an array of meeting time intervals, where each interval is represented as a pair [start, end]. The function should return true if a person can attend all meetings without any overlaps, otherwise return false."
"""



# def canAttendMeetings(time_intervals):
#     """
    
#     """
#     for i in range(len(time_intervals)):
#         for j in range(len(time_intervals)):
#             if i == j:
#                 # Both the slots index are same
#                 continue
#             if time_intervals[i][0] == time_intervals[j][0] and time_intervals[i][1] == time_intervals[j][1]:
#                 # Start and end time for the time slot is overlapping and hence return false
#                 print("False: Because overapping")
#                 return False
            
#     print("True")
#     return True

# def canAttendMeetings(time_intervals):
#     time_intervals.sort(key=lambda x:x[0])
#     print(time_intervals)

#     for i in range(1,len(time_intervals)):
#         previous_end_time = time_intervals[i-1][1]
#         next_start_time = time_intervals[i][0]
#         print(previous_end_time,next_start_time)
#         if next_start_time < previous_end_time:
#             # print(end_time,next_start_time)
#             print("Overlapp")
#             return False
#     return True





time_intervals = [[111, 211], [112,113],[1,2],[12,20]] # return false
time_intervals.sort()
print(time_intervals)
# time_intervals = [[1, 7], [4,6]]
# canAttendMeetings(time_intervals)
