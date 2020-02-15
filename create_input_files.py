from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='coco',
                       karpathy_json_path='/home/xilini/a-PyTorch-Tutorial-to-Image-Captioning/data/dataset_coco.json',
                       image_folder='/home/xilini/vis-data/',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='/home/xilini/a-PyTorch-Tutorial-to-Image-Captioning/data/',
                       max_len=50)
