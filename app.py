from PIL import Image
import glob
import os

# Function for creating new directory
def create_new_dir(dir):
    try:
        os.mkdir(dir)
    except:
        print("File already exist\n...")
        print("Skipping creating directory\n...")

# Function for resizing the image
def resizer(dir, new_dir):
    create_new_dir(new_dir)
    frames = [Image.open(image) for image in glob.glob(f"{dir}/*.jpg")]
    height = 550 # Adjust to the desired size
    width = 150 # Adjust to the desired size
    for idx, image in enumerate(glob.glob(f"{dir}/*.jpg")):
        frames[idx] = frames[idx].resize((height, width), Image.ANTIALIAS)
        frames[idx].save(f"{new_dir}/{str(idx)}.jpg")


# Function for creating gif from collection of image
def make_gif(frame_dir):
    frames = [Image.open(image) for image in glob.glob(f"{frame_dir}/*.jpg")]
    frame_one = frames[0]
    frame_one.save("My_Gif_rand_f.gif", format="GIF", append_images=frames,
                    save_all=True, duration=500, loop=0)
    print(f"Process completed, gif saved")

if __name__ == "__main__":
    # resizer("quote", "new")
    make_gif("quote")

