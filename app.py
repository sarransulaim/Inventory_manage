import streamlit as st
import uuid # To give each item a unique ID

st.set_page_config(layout="wide", page_title="Store Task Manager")

# --- DATA INITIALIZATION ---
# Using session_state to act as a temporary, in-memory database.
if 'data' not in st.session_state:
    st.session_state.data = {
        "Grocer A": {
            "password": "123",
            "lists": {
                "Candy": [
                    {'id': uuid.uuid4(), 'name': 'Snickers Bar', 'status': 'pending', 'assigned_to': None}
                ],
                "Drinks": [
                    {'id': uuid.uuid4(), 'name': 'Coke Zero', 'status': 'pending', 'assigned_to': None}
                ],
            },
            "members": [
                {"name": "Alice", "phone": "555-0101"},
                {"name": "Bob", "phone": "555-0102"},
            ]
        }
    }
if 'logged_in_group' not in st.session_state:
    st.session_state.logged_in_group = None


# --- HELPER FUNCTIONS ---
def simulate_notification(group_name, message):
    """
    Simulates sending a notification. In this test app, it shows an on-screen toast.
    """
    st.toast(f"📢 {message}")


# --- SIDEBAR FOR LOGIN & GROUP MANAGEMENT ---
st.sidebar.title("🏬 Store Management")

if st.session_state.logged_in_group:
    st.sidebar.success(f"Logged in to: **{st.session_state.logged_in_group}**")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in_group = None
        st.rerun()
else:
    st.sidebar.subheader("Login to Existing Store")
    with st.sidebar.form("login_form"):
        groups = list(st.session_state.data.keys())
        selected_group = st.selectbox("Select Store", groups)
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")

        if login_button:
            if selected_group and st.session_state.data[selected_group]['password'] == password:
                st.session_state.logged_in_group = selected_group
                st.rerun()
            else:
                st.sidebar.error("Incorrect password.")

    st.sidebar.subheader("Create a New Store")
    with st.sidebar.form("create_group_form"):
        new_group_name = st.text_input("New Store Name")
        new_password = st.text_input("Set Password", type="password")
        create_button = st.form_submit_button("Create Store")

        if create_button and new_group_name and new_password:
            if new_group_name in st.session_state.data:
                st.sidebar.warning("A store with this name already exists.")
            else:
                st.session_state.data[new_group_name] = {"password": new_password, "lists": {}, "members": []}
                st.session_state.logged_in_group = new_group_name
                st.rerun()

# --- MAIN APP VIEW (Only shows if logged in) ---
if not st.session_state.logged_in_group:
    st.info("👋 Welcome! Please log in or create a new store using the sidebar.")
else:
    group_name = st.session_state.logged_in_group
    st.header(f"Profile for: {group_name}")

    tab1, tab2 = st.tabs(["📝 Lists & Items", "👥 Manage People"])

    # --- TAB 1: LISTS AND ITEMS ---
    with tab1:
        st.subheader("Create a New List")
        with st.form("new_list_form"):
            new_list_name = st.text_input("List Name (e.g., Dairy, Produce)")
            if st.form_submit_button("Add List"):
                if new_list_name and new_list_name not in st.session_state.data[group_name]['lists']:
                    st.session_state.data[group_name]['lists'][new_list_name] = []
                    simulate_notification(group_name, f"New list '{new_list_name}' was created.")
                    st.rerun()
                else:
                    st.warning("List name cannot be empty or already exist.")

        st.divider()
        st.subheader("Current Lists")
        if not st.session_state.data[group_name]['lists']:
            st.info("No lists created yet. Add one above!")

        for list_name, items in st.session_state.data[group_name]['lists'].items():
            with st.expander(f"**{list_name}** ({len(items)} items)", expanded=True):
                with st.form(f"add_item_{list_name}"):
                    new_item_name = st.text_input("New Item Name", key=f"new_item_{list_name}")
                    if st.form_submit_button("Add Item"):
                        if new_item_name:
                            item = {'id': uuid.uuid4(), 'name': new_item_name, 'status': 'pending', 'assigned_to': None}
                            st.session_state.data[group_name]['lists'][list_name].append(item)
                            simulate_notification(group_name, f"'{new_item_name}' added to '{list_name}'.")
                            st.rerun()

                st.markdown("---")
                for i, item in enumerate(items):
                    item_cols = st.columns((4, 2, 2)) # Columns for Item Info, Status, and Actions button

                    with item_cols[0]:
                        st.write(f"**{item['name']}**")

                    with item_cols[1]:
                        status_color = {"pending": "grey", "taken": "orange", "complete": "green"}[item['status']]
                        assigned_to = f"👤 {item['assigned_to']}" if item['assigned_to'] else ""
                        st.markdown(f"<span style='color:{status_color};'>● {item['status'].capitalize()}</span> {assigned_to}", unsafe_allow_html=True)
                    
                    with item_cols[2]:
                        # --- NEW: Popover for all item actions ---
                        with st.popover("Actions ▾"):
                            st.markdown(f"**Options for {item['name']}**")
                            
                            # --- Assign Action ---
                            members = st.session_state.data[group_name]['members']
                            if members:
                                with st.form(key=f"assign_form_{item['id']}"):
                                    member_name = st.selectbox("Assign to:", [m['name'] for m in members])
                                    if st.form_submit_button("Confirm Assignment", use_container_width=True):
                                        item['assigned_to'] = member_name
                                        item['status'] = 'taken'
                                        simulate_notification(group_name, f"'{item['name']}' assigned to {member_name}.")
                                        st.rerun()
                            else:
                                st.caption("Add people in the 'Manage People' tab to assign tasks.")

                            # --- Move Action ---
                            other_lists = [l for l in st.session_state.data[group_name]['lists'] if l != list_name]
                            if other_lists:
                                with st.form(key=f"move_form_{item['id']}"):
                                    target_list = st.selectbox("Move to:", other_lists)
                                    if st.form_submit_button("Confirm Move", use_container_width=True):
                                        moved_item = st.session_state.data[group_name]['lists'][list_name].pop(i)
                                        st.session_state.data[group_name]['lists'][target_list].append(moved_item)
                                        simulate_notification(group_name, f"'{item['name']}' moved to '{target_list}'.")
                                        st.rerun()

                            # --- Quick Actions ---
                            if st.button("Mark Complete ✅", key=f"complete_{item['id']}", use_container_width=True):
                                item['status'] = 'complete'
                                simulate_notification(group_name, f"'{item['name']}' was marked complete.")
                                st.rerun()

                            if st.button("Delete Item 🗑️", key=f"delete_{item['id']}", type="primary", use_container_width=True):
                                deleted_item_name = st.session_state.data[group_name]['lists'][list_name].pop(i)['name']
                                simulate_notification(group_name, f"'{deleted_item_name}' was deleted.")
                                st.rerun()
                    st.divider()

    # --- TAB 2: MANAGE PEOPLE ---
    with tab2:
        st.subheader("Add a New Person to the Group")
        with st.form("new_member_form"):
            new_member_name = st.text_input("Person's Name")
            new_member_phone = st.text_input("Person's Phone Number (for notifications)")
            if st.form_submit_button("Add Person"):
                if new_member_name and new_member_phone:
                    st.session_state.data[group_name]['members'].append({"name": new_member_name, "phone": new_member_phone})
                    st.rerun()
                else:
                    st.warning("Name and phone number are required.")

        st.divider()
        st.subheader("Current People in this Group")
        if not st.session_state.data[group_name]['members']:
            st.info("No people have been added to this group yet.")
        else:
            for i, member in enumerate(st.session_state.data[group_name]['members']):
                mem_cols = st.columns((2, 2, 1))
                mem_cols[0].write(f"**Name:** {member['name']}")
                mem_cols[1].write(f"**Phone:** {member['phone']}")
                if mem_cols[2].button("Remove", key=f"remove_member_{i}"):
                    st.session_state.data[group_name]['members'].pop(i)
                    st.rerun()
