date=int(input("Enter Date:"))
month=input("Enter month:")
if(month=="december"):
    a='sagittarius' if(date < 22) else 'Capricorn'
elif(month=="january"):
    a='Capricorn' if(date < 20) else 'Aquarius'
elif(month=="february"):
    a='Aquarius' if(date<19) else 'Pisces'
elif(month=="march"):
    a='Pisces' if(date<21) else 'Aries'
elif(month=="april"):
    a='Aries' if(date<20) else 'Taurus'
elif(month=="may"):
    a='Taurus' if(date<21) else 'Gemini'
elif(month=="june"):
    a='Gemini' if(date<21) else 'Cancer'
elif(month=="july"):
    a='Cancer' if(date<23) else 'Leo'
elif(month=="august"):
    a='Leo' if(date<23) else 'Virgo'
elif(month=="september"):
    a='Virgo' if(date<23) else 'Libra'
elif(month=="october"):
    a='Libra' if(date<23) else 'Scorpio'
elif(month=="november"):
    a='Scorpio' if(date<22) else 'sagittarius'
else:
    a='Invalid month'
print(a)
