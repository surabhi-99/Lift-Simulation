# Lift Management System

## Overview

This project simulates the operation of multiple lifts within a multi-floor building, optimizing for minimal wait and travel time. It demonstrates robust backend design principles such as modularity, extensibility, and efficient data handling.

## Features

- **Multiple Lifts:** Supports any number of lifts.
- **Dynamic Requests:** Can handle lift requests at any point in time.
- **Efficient Routing:** Chooses the nearest available lift to minimize wait times.
- **State Management:** Tracks and updates the state of each lift (open or closed).

## Modules

### Lift

- **Attributes:**
  - `id`: Unique identifier for each lift.
  - `current_floor`: Current floor of the lift.
  - `destination_floor`: Target floor for the lift.
  - `state`: Current state of the lift door (open or closed).
  - `max_floors`: Maximum number of floors the lift can service.
  - `direction`: Current travel direction of the lift (up, down, or none).
  - `time_taken`: Total time taken for operations since last reset.

- **Methods:**
  - `assign_request()`: Assigns a new travel request to the lift.
  - `move()`: Moves the lift one floor per call towards its destination.
  - `open_or_close_door()`: Manages the opening and closing of the lift door.

### Building

- **Attributes:**
  - `lifts`: List of lifts in the building.
  - `num_floors`: Number of floors in the building.
  - `requests`: Queue of pending lift requests.

- **Methods:**
  - `process_request()`: Adds new lift requests to the queue.
  - `find_closest_lift()`: Finds the nearest available lift for a new request.
  - `simulate()`: Processes all requests and outputs lift movements and states sequentially.


## Extensibility

The system has been designed with extensibility in mind. Key areas for expansion include:

- **Priority Handling:** Incorporating priority levels for requests, such as emergency or VIP, to ensure faster service where needed.
- **Energy Efficiency Modes:** Implementing energy-saving strategies, such as sending nearest idle lifts or grouping close-proximity calls.
- **Real-Time Updates:** Enhancing the system to allow for real-time changes to requests or lift operations, improving responsiveness to dynamic conditions.

## Limitations

While the system is robust, there are some limitations:

- **Routing Simplicity:** The current routing algorithm selects the nearest available lift but does not consider load balancing across lifts, which could lead to inefficiencies during peak times.
- **Lack of Real-Time Interruptions Handling:** The system does not currently support altering lift routes mid-operation in response to new or cancelled requests.

## Future Enhancements

Plans for future updates to address limitations and add new features include:

- **Advanced Scheduling Algorithm:** To more evenly distribute lift usage and reduce wait times, particularly during high traffic periods.
- **Emergency Handling and Accessibility Support:** Adding functionality for emergency situations and improving accessibility for users with disabilities.
- **User Interface for Real-Time Control:** Developing a user interface to monitor and control lift operations in real-time, offering greater flexibility and efficiency.

These enhancements aim to make the Lift Management System more efficient, user-friendly, and adaptable to a wide range of building configurations and user needs.

