from recommendations import critics
from src import recommendations
print critics['Lisa Rose']['Lady in the Water']

critics['Toby']['Snake on a plane']=4.5
print critics['Toby']

print recommendations.sim_distance(critics, 'Lisa Rose', 'Gene Seymour')