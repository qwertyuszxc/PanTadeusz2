import json
movie = {
    'Premier':2013,
    'Budget':'$46mil',
    'Main_role':"Jake Gyllenhaal",
    'Director':'Denis Villeneuve',
    'Rotten_tomato_score':'81%'
}
out_file = open('movie.json','w')
json.dump(movie,out_file,indent=6)
out_file.close()