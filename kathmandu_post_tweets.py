import twint

kat = twint.Config()

kat.Username = "kathmandupost"
kat.Since = "2019-05-07"

# kat.Format = "Username: {username} | Tweet : {tweet}"

kat.Limit = 1

kat.Pandas = True

twint.run.Search(kat)