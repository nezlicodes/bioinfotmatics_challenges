import matplotlib.pyplot as plt;
import matplotlib_venn as venn;
S ={1,2,3}
P = {-1,3, 4}
venn.venn2([S,P], set_labels=('S','P'))
plt.show()