from pathlib import Path  
import imageio
from wordcloud import WordCloud

t = Path("RomeoAndJuliet.txt").read_text()

mask = imageio.imread("mask_heart.png")

wc = WordCloud(colormap = "prism", mask = mask, background_color = "white")

wc = wc.generate(t)

wc = wc.to_file("RomeoJuliet.png")








