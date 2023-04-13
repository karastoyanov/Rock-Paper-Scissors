import pysnc

client = pysnc.ServiceNowClient('dev109438', ('admin', 'LrmsjVJB@8^3'))
user_name = 'Test User 2'

gr_custom_table = client.GlideRecord('u_rock_paper_scissors_users')
gr_custom_table.query()
gr_custom_table.next()

for gr in gr_custom_table:
    if gr.get_display_value('u_user_name') == user_name:
        print('Found')