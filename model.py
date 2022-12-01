import argparse
from fastrcnn import get_model

def get_model():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_lbl', default="/labeled/labeled", metavar='DATA_PATH_LBL', type=str, help="Default path for labeled data; default used is '/labeled/labeled'; note toy set's is 'labeled_data/'")
    #parser.add_argument('--path_unlbl', default="/unlabeled/unlabeled", metavar='DATA_PATH_UNLBL', type=str, help="Default path for unlabeled data; default used is'/unlabeled/unlabeled'; note toy set's is 'unlabeled_data/'")
    #parser.add_argument('--shuffle', action='store_true', help="Shuffle data toggle")
    #parser.add_argument('-voff', '--verbose_off', action='store_false', help="Verbose mode toggle")
    parser.add_argument('-c', '--classes', default=100, type=int, metavar='NUM_CLASSES', help='Number of classes; default is 100')

    #model
    #parser.add_argument('--train_backbone', action='store_true', help='Train backbone toggle')
    parser.add_argument('-o', '--output_size', default=1, type=int, help="Output size for the backbone")
    parser.add_argument('-bb', '--backbone', default="SimCLR", type=str, metavar='BACKBONE', help = "Backbone to use; default is SimCLR. Set to 'None' for mobilenet_v2.")
    parser.add_argument('-bs', '--batch_size', default=32, type=int, metavar='BATCH_SIZE', help='Batch size to use')
    #parser.add_argument('-e', '--epochs', default=5, metavar='EPOCHS', type=int, help="Default number of epochs")
    #parser.add_argument('-lr', '--learn_rate', default=0.001, metavar='LEARN_RATE', type=float, help="Default learning rate")
    #parser.add_argument('-mom', '--momentum', default=0.9, metavar='MOMENTUM', type=float, help="Default momentum")
    #parser.add_argument('-dk', '--weight_decay', default=0.0005, metavar='WEIGHT_DECAY', type=float, help="Default weight decay")
    #parser.add_argument('-p', '--print_freq', default=200, metavar='PRINT_FREQ', type=int, help="Default print frequency")
    #parser.add_argument('-s', '--step', default=50, metavar='SCHEDULER_STEP', type=int, help="Default step size for scheduler")
    #parser.add_argument('-g', '--gamma', default=0.2, metavar='SCHEDULER_GAMMA', type=float, help="Default gamma factor for scheduler")
    #parser.add_argument('-f', '--freeze', action='store_true', help='Freeze backbone weights; default is False')

    #backbone args
    #parser.add_argument('-bbe','--backbone_epochs', default=10, metavar='BACKBONE_EPOCHS', type=int, help="Default number of backbone epochs")
    parser.add_argument('-bbcoff','--backbone_cuda_off', action='store_false', help="Toggle CUDA for backbone training")
    parser.add_argument('-bbsd','--backbone_seed', default=77777, metavar='BACKBONE_SEED', type=int, help="Backbone seed for reproducibility")
    #parser.add_argument('-bbimg','--backbone_img_size', default=224, metavar='BACKBONE_IMG_SIZE', type=int, help="Backbone img size")
    parser.add_argument('-bbsv','--backbone_save_directory', default='saved_models/', metavar='BACKBONE_SAVE_DIR_PATH', type=str, help="Backbone save checkpoint directory path")
    parser.add_argument('-bblp','--backbone_load_pretrained', action='store_true', help="Backbone load pretraining")
    parser.add_argument('-bbg','--backbone_grad_accumulate_steps', type=int, default = 5, metavar='BACKBONE_GRAD_ACCUM_STEPS', help="Backbone gradient accumulation steps")
    parser.add_argument('-bbbs', '--backbone_batch_size', default=96, type=int, metavar='BACKBONE_BATCH_SIZE', help='Backbone batch size to use')
    parser.add_argument('-bbemb','--backbone_embedding_size', type=int, default = 128, metavar='BACKBONE_EMBED_SIZE', help='Backbone embedding size')
    parser.add_argument('-bblr','--backbone_lr', type=float, default = 3e-4, metavar='BACKBONE_ADAM_LEARN_RATE', help='Backbone learning rate for ADAM')
    parser.add_argument('-bbdk','--backbone_weight_decay', type=float, default = 1e-6, metavar='BACKBONE_WEIGHT_DECAY', help='Backbone weight decay')
    parser.add_argument('-bbtmp','--backbone_temperature', type=float, default=0.1, metavar='BACKBONE_TEMP', help='Backbone temperature parameter (set to 0.1 or 0.5)')
    parser.add_argument('-bbcp','--backbone_checkpoint_path', default='./SimCLR_ResNet18.ckpt', metavar='BACKBONE_CHECKPOINT_PATH', type=str, help="Backbone checkpoint path")
    parser.add_argument('-bbr','--backbone_resume', action='store_true', help="Backbone resume training from checkpoint; default is False")
    args = parser.parse_args()

    model = get_model(args, backbone=args.backbone, num_classes=args.classes)
    
    return model