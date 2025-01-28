import requests
from datetime import datetime, timezone
import os
from dotenv import load_dotenv
import json

load_dotenv()
access_token = os.getenv('CANVAS_ACCESS_TOKEN')
base_url = os.getenv('CANVAS_BASE_URL')

# Set up the headers for authentication
headers = {
    'Authorization': f'Bearer {access_token}'
}

def get_courses():
    """
    Retrieve the list of courses the user is enrolled in.
    """
    url = f'{base_url}/api/v1/courses'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_upcoming_events():
    """
    Retrieve upcoming events for the user, including assignments.
    """
    url = f'{base_url}/api/v1/users/self/upcoming_events'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_assignments(course_id):
    """
    Retrieve assignments for a specific course.
    """
    url = f'{base_url}/api/v1/courses/{course_id}/assignments'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def filter_upcoming_assignments(assignments):
    """
    Filter assignments to include only those with due dates in the future.
    """
    upcoming = []
    now = datetime.now(timezone.utc)
    for assignment in assignments:
        due_at = assignment.get('due_at')
        if due_at:
            due_date = datetime.fromisoformat(due_at.replace('Z', '+00:00'))
            if due_date > now:
                upcoming.append(assignment)
    return upcoming