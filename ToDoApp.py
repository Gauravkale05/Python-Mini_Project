import streamlit as st

def disp_task(tasks):
    """Display the to-do list."""
    if tasks:
        st.subheader("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            st.write(f"{i}. {task}")
    else:
        st.subheader("Your To-Do List is Empty.")

# Initialize session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

st.title("To-Do List App")

# Input for adding a new task
new_task = st.text_input("Enter a new task:")
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"Task '{new_task}' added.")
    else:
        st.warning("Task cannot be empty!")

# Display current tasks if available
if st.session_state.tasks:
    disp_task(st.session_state.tasks)

# Deleting a task
if st.session_state.tasks:
    task_to_delete = st.number_input("Enter task number to delete:", min_value=1, max_value=len(st.session_state.tasks), step=1, format="%d")
    if st.button("Delete Task"):
        removed_task = st.session_state.tasks.pop(task_to_delete - 1)
        st.success(f"Task '{removed_task}' removed.")
        st.rerun()
else:
    st.warning("No tasks available to delete.")
