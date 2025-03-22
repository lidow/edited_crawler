def calculate_min_time(task):
    # Constants
    BUTTON_PRESS_TIME = 1
    INITIAL_POSITION = 1

    # Track time and positions
    task_time = 0
    robot_state = {
        'o': {'total_time': 0, 'position': INITIAL_POSITION},
        'b': {'total_time': 0, 'position': INITIAL_POSITION}
    }

    for move in task:
        robot = move[0].lower()
        target = int(move[1:])

        # Calculate move time and update state
        move_time = abs(target - robot_state[robot]['position'])
        robot_time = max(task_time - robot_state[robot]['total_time'], move_time) + BUTTON_PRESS_TIME

        # Update position and times
        robot_state[robot]['position'] = target
        task_time += robot_time - (task_time - robot_state[robot]['total_time'])
        robot_state[robot]['total_time'] += robot_time

    return task_time


if __name__ == "__main__":

    print("Case 1")
    task = ["o2", "b1", "b2", "o4"]
    print(f"Input: {task}")
    result = calculate_min_time(task)
    print(f"Minimum time required: {result} seconds")

    print("\n\nCase 2")
    task = ["o5", "o8", "b100"]
    print(f"Input: {task}")
    result = calculate_min_time(task)
    print(f"Minimum time required: {result} seconds")

    print("\n\nCase 3")
    task = ["b2", "b1"]
    print(f"Input: {task}")
    result = calculate_min_time(task)
    print(f"Minimum time required: {result} seconds")

    print("\n\nCase 4")
    task = ["b2", "b1", "o3", "o6", "b2"]
    print(f"Input: {task}")
    result = calculate_min_time(task)
    print(f"Minimum time required: {result} seconds")