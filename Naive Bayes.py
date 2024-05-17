import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import Button
from matplotlib.gridspec import GridSpec
from tabulate import tabulate
import csv

edi = []
edi1 = []
x = [bool(0), bool(1)]

def huruf_terbanyak(array):
    concatenated_string = ''.join(array)

    counter = Counter(concatenated_string)

    huruf_paling_banyak = counter.most_common(1)[0][0]

    return huruf_paling_banyak

def a(i):
    def on_button_click(event):
        percentage_str = '{:.2%}'.format(hd_e[i])
        edi.append(hd_e[i])
        edi1.append(percentage_str)
        x[0] = True
        plt.close()
    return on_button_click

def b(i):
    def on_button_click(event):
        percentage_str = '{:.2%}'.format(hd_p[i])
        edi.append(hd_p[i])
        edi1.append(percentage_str)
        x[0] = True
        plt.close()
    return on_button_click

def c(event):
    x[1] = True
    plt.close()

def on_button_click_d(event):
    x[1] = False
    plt.close()

file_csv = '22081010141_Steven Nathan Kusuma_Bayes.csv'
data_frame = pd.read_csv(file_csv)

key = data_frame['edible/poisonous']
cap_shape = data_frame['cap-shape']
cap_surface = data_frame['cap-surface']
cap_color = data_frame['cap-color']
bruises = data_frame['Bruises']
odor = data_frame['Odor']
gill_att = data_frame['gill-attachment']
gill_spacing = data_frame['gill-spacing']
gill_size = data_frame['gill-size']
gill_color = data_frame['gill-color']
stalk_shape = data_frame['stalk-shape']
stalk_root = data_frame['stalk-root']
stalk_surface_above = data_frame['stalk-surface-above-ring']
stalk_surface_below = data_frame['stalk-surface-below-ring']
stalk_color_above = data_frame['stalk-color-above-ring']
stalk_color_below = data_frame['stalk-color-below-ring']
veil_type = data_frame['veil-type']
veil_color = data_frame['veil-color']
ring_number = data_frame['ring-number']
ring_type = data_frame['ring-type']
spore_print_color = data_frame['spore-print-color']
population = data_frame['Population']
habitat = data_frame['Habitat']

n =  len(key)
poison = 0

for i in key:
    if i == "p":
        poison = poison + 1
edible = n - poison

#p(H)
h_edible = edible/n
h_poison = poison/n

#p(D|H)
dh_e = []
dh_p = []
e = []
p = []
for i in range(len(data_frame.iloc[0])-1):
    count = 0
    e.append(0)
    for j in range(n):
        if data_frame.iloc[j, i] == huruf_terbanyak(data_frame.iloc[:, i]):
            count = count + 1
            if key[j] == "e":
                e[i] = e[i] + 1
    p.append(count - e[i])
    dh_e.append(e[i]/edible)
    dh_p.append(p[i]/poison)

#p(D)
d = []
for i in range(len(data_frame.iloc[0])-1):
    count = 0
    for j in range(n):
        if data_frame.iloc[j, i] == huruf_terbanyak(data_frame.iloc[:, i]):
            count = count + 1
    d.append(count/n)

#p(H|D)
hd_e = []
hd_p = []
for i in range(len(data_frame.iloc[0])-1):
    hd_e.append(h_edible*dh_e[i]/d[i])
    hd_p.append(h_poison*dh_p[i]/d[i])

cap_shape_a = 'cap_shape_a.jpg'
cap_surface_a = 'cap_surface_a.jpg'
cap_color_a = 'cap_color_a.png'
bruises_a = 'bruises_a.jpg'
odor_a = 'odor_a.png'
gill_att_a = 'gill_att_a.png'
gill_spacing_a = 'gill_spacing_a.png'
gill_size_a = 'gill_size_a.png'
gill_color_a = 'gill_color_a.jpeg'
stalk_shape_a = 'stalk_shape_a.jpg'
stalk_root_a = 'stalk_root_a.jpg'
stalk_above_surface_a = 'stalk_above_surface_a.png'
stalk_below_surface_a = 'stalk_below_surface_a.png'
stalk_above_color_a = 'stalk_above_color_a.png'
stalk_below_color_a = 'stalk_below_color_a.png'
veil_type_a = 'veil_type_a.png'
veil_color_a = 'veil_color_a.png'
ring_number_a = 'ring_number_a.png'
ring_type_a = 'ring_type_a.png'
spore_print_color_a = 'spore_print_color_a.png'
population_a = 'population_a.png'
habitat_a = 'habitat_a.png'

cap_shape_b = 'cap_shape_b.jpg'
cap_surface_b = 'cap_surface_b.jpg'
cap_color_b = 'cap_color_b.png'
bruises_b = 'bruises_b.png'
odor_b = 'odor_b.png'
gill_att_b = 'gill_att_b.png'
gill_spacing_b = 'gill_spacing_b.png'
gill_size_b = 'gill_size_b.png'
gill_color_b = 'gill_color_b.png'
stalk_shape_b = 'stalk_shape_b.jpg'
stalk_root_b = 'stalk_root_b.jpg'
stalk_above_surface_b = 'stalk_above_surface_b.png'
stalk_below_surface_b = 'stalk_below_surface_b.png'
stalk_above_color_b = 'stalk_above_color_b.png'
stalk_below_color_b = 'stalk_below_color_b.png'
veil_type_b = 'veil_type_b.png'
veil_color_b = 'veil_color_b.png'
ring_number_b = 'ring_number_b.png'
ring_type_b = 'ring_type_b.png'
spore_print_color_b = 'spore_print_color_b.png'
population_b = 'population_b.png'
habitat_b = 'habitat_b.png'

mario = 'mario.png'
hypno = 'Hypno.png'

edible_s = mpimg.imread(mario)
poison_s = mpimg.imread(hypno)
 
gambar1 = [mpimg.imread(cap_shape_a), mpimg.imread(cap_surface_a), mpimg.imread(cap_color_a), mpimg.imread(bruises_a), mpimg.imread(odor_a), mpimg.imread(gill_att_a), mpimg.imread(gill_spacing_a), mpimg.imread(gill_size_a), mpimg.imread(gill_color_a), mpimg.imread(stalk_shape_a), mpimg.imread(stalk_root_a), mpimg.imread(stalk_above_surface_a), mpimg.imread(stalk_below_surface_a), mpimg.imread(stalk_above_color_a), mpimg.imread(stalk_below_color_a), mpimg.imread(veil_type_a), mpimg.imread(veil_color_a), mpimg.imread(ring_number_a), mpimg.imread(ring_type_a), mpimg.imread(spore_print_color_a), mpimg.imread(population_a), mpimg.imread(habitat_a)]
gambar2 = [mpimg.imread(cap_shape_b), mpimg.imread(cap_surface_b), mpimg.imread(cap_color_b), mpimg.imread(bruises_b), mpimg.imread(odor_b), mpimg.imread(gill_att_b), mpimg.imread(gill_spacing_b), mpimg.imread(gill_size_b), mpimg.imread(gill_color_b), mpimg.imread(stalk_shape_b), mpimg.imread(stalk_root_b), mpimg.imread(stalk_above_surface_b), mpimg.imread(stalk_below_surface_b), mpimg.imread(stalk_above_color_b), mpimg.imread(stalk_below_color_b), mpimg.imread(veil_type_b), mpimg.imread(veil_color_b), mpimg.imread(ring_number_b), mpimg.imread(ring_type_b), mpimg.imread(spore_print_color_b), mpimg.imread(population_b), mpimg.imread(habitat_b)]
suptitle = ['Bentuk kepala jamurnya seperti apa?', 'Tekstur kepala jamurnya seperti apa?', 'Warna kepala jamurnya seperti apa?', 'Apakah ada memar?', 'Baunya seperti apa?', 'Gill yang menempel seperti apa?', 'Jarak gill nya seperti apa?', 'Ukuran gill nya seperti apa?', 'Warna gillnya apa?', 'Bentuk batangnya seperti apa?', 'Akarnya seperti apa?', 'Tekstur batang diatas ring seperti apa?', 'Tekstur batang dibawah ring seperti apa?', 'Warna batang diatas ring apa?', 'Warna batang dibawah ring apa?', 'Tipe veilnya seperti apa?', 'Warna veilnya apa?', 'Banyaknya jumlah ring berapa?', 'Tipe ringnya seperti apa?', 'Warna spore printnya apa?', 'Apakah hidup berkoloni?', 'Dimana anda menemukannya?',]
title_a = ['Convex', 'Smooth', 'Putih', 'Ya', 'Manis', 'Free', 'Close', 'Broad', 'Putih', 'Equal', 'Bulbuos', 'Smooth', 'Smooth', 'Putih', 'Putih', 'Partial', 'Putih', 'Satu', 'Superior', 'Coklat', 'Berkoloni', 'Lapangan rumput']
title_b = ['Lonceng', 'Berambut', 'Kuning', 'Tidak', 'Menyengat', 'Terikat', 'Distant', 'Narrow', 'Pink', 'Club', 'Rhizoid', 'Fibrillose', 'Squamulose', 'Kuning', 'Kuning', 'Annulus', 'Kuning', 'Dua', 'Median', 'Cream', 'Individu', 'Hutan']

while x[1] == True:
    x[1] = False
    for i in range(len(data_frame.iloc[0])-1):
        x[0] = False
        fig = plt.figure()
        gs = GridSpec(2, 2, height_ratios=[1, 0.1])
        fig.suptitle(suptitle[i])

        # Menambahkan subplot di baris pertama untuk gambar
        ax1 = fig.add_subplot(gs[0])
        ax1.imshow(gambar1[i])
        ax1.axis('off')  

        ax3 = fig.add_subplot(gs[1])
        ax3.imshow(gambar2[i])
        ax3.axis('off')  

        # Menambahkan subplot di baris kedua untuk tombol
        ax2 = fig.add_subplot(gs[2])
        button1 = Button(ax2, title_a[i], color="#2e6deb", hovercolor="#6996ef")
        button1.on_clicked(a(i))

        ax4 = fig.add_subplot(gs[3])
        button2 = Button(ax4, title_b[i], color="#2e6deb", hovercolor="#6996ef")
        button2.on_clicked(b(i))

        plt.show()
        if x[0] == False:
            break
    
    with open(file_csv, 'r') as file:
        # Membuat objek pembaca CSV
        csv_reader = csv.reader(file)

        # Membaca baris pertama (header)
        headers = next(csv_reader)[:22]
        
    # Membuat tabel dengan tabulate
    headers1 = headers[:12]
    headers2 = headers[12:22]
    data1 = edi1[:12]
    data2 = edi1[12:22]
    table = tabulate([data1], headers1, tablefmt="fancy_grid")
    table1 = tabulate([data2], headers2, tablefmt="fancy_grid")

    # Menampilkan tabel
    print(table)
    print(table1)

    sum = 0
    for i in range(len(edi)):
        sum = edi[i] + sum
    prediksi = sum/22
    prediksi1 = ['{:.2%}'.format(prediksi)]
    prediksi2 = ['{:.2%}'.format(1 - prediksi)]
    
    header_e = ["Aman"]
    header_p = ["Beracun"]
    
    print("Prediksi: ")
    if prediksi > 0.5:
        table3 = tabulate([prediksi1], header_e, tablefmt="fancy_grid")
        table4 = tabulate([prediksi2], header_p, tablefmt="fancy_grid")
        print(table3)
        print(table4)
    else: 
        table3 = tabulate([prediksi1], header_p, tablefmt="fancy_grid")
        table4 = tabulate([prediksi2], header_e, tablefmt="fancy_grid")
        print(table3)
        print(table4)
        
    edi.clear()

    if x[0] == True:
        fig = plt.figure(figsize=(8, 8))
        gs = GridSpec(3, 1, height_ratios=[2, 0.1, 0.1])

        if prediksi > 0.5:
            ax1 = fig.add_subplot(gs[0])
            fig.suptitle('Jamur anda dapat dimakan, Apa anda ingin mengulang program?')
            ax1.imshow(edible_s)
            ax1.axis('off')  
        else:
            ax1 = fig.add_subplot(gs[0]) 
            fig.suptitle('Jamur anda beracun, Apa anda ingin mengulang program?')
            ax1.imshow(poison_s)
            ax1.axis('off')  

        ax2 = fig.add_subplot(gs[1])
        button1 = Button(ax2, 'YA', color="#2e6deb", hovercolor="#6996ef")
        button1.on_clicked(c)
        
        ax3 = fig.add_subplot(gs[2])
        button2 = Button(ax3, 'TIDAK', color="#2e6deb", hovercolor="#e81123")
        button2.on_clicked(on_button_click_d) 
        plt.show()
