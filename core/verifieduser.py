'''

import twint

c = twint.Config()
c.Username = "catalinmpit"
c.Custom["user"] = ["id", "username","verified"]
c.Format = "ID : {id} | Username : {username} | Is_Verified : {verified}"
c.Output = "username01.json"
c.Store_json = True

twint.run.Lookup(c)
'''

import twint

#list_screen_name=['GovernorMasari','brajnilutkarsh','narendramodi','brajnilutkarsh']

def get_user_info(screen_name):
    c = twint.Config()
    c.Username = screen_name
    c.Pandas = True
    c.User_full = True
    twint.run.Lookup(c)
    Users_df = twint.storage.panda.User_df
    Users_df.drop_duplicates(subset ="name", keep = 'last', inplace = True) 
    return Users_df

def verify_list(list1): 
    for i in list1:
        Users_df = get_user_info(i)
        verify_df=Users_df.loc[:, ['username','verified']]
        verify_df.set_index('username',inplace=True)
    return (verify_df)

#ans = verify_list(list_screen_name)