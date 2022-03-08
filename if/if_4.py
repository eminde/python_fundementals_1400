print("======================================")

have_umbrella = True
rain_level = 6
have_hood = True
is_workday = False


prepared_for_weather = (
    (have_umbrella
    or (rain_level < 5 and have_hood))
    or ((not rain_level > 0) and is_workday))

print(prepared_for_weather)
print("======================================")