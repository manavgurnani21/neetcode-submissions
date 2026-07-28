class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) < 2:
            return len(position)
        
        vehicle_directory = {}

        # building time-wise map
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            vehicle_directory[position[i]] = time
        
        sorted_times = dict(sorted(vehicle_directory.items(), reverse=True))

        lead_time = 0
        fleet_count = 0
        for vehicle_pos in sorted_times:
            if sorted_times[vehicle_pos] > lead_time:
                print(f"Current time: {sorted_times[vehicle_pos]}, Lead Car Time: {lead_time}")
                fleet_count += 1
                lead_time = sorted_times[vehicle_pos]

        return fleet_count