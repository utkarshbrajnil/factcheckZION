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

c = twint.Config()
c.Username = "catalinmpit"
c.Pandas = True
c.User_full = True

twint.run.Lookup(c)


Users_df = twint.storage.panda.User_df