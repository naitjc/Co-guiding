# -*- coding: utf-8 -*-#
import argparse
import torch

parser = argparse.ArgumentParser(description='HGAT')

# Dataset and Other Parameters
parser.add_argument('--data_dir', '-dd', help='dataset file path', type=str, default='./Dataset/MSATIS')
parser.add_argument('--save_dir', '-sd', type=str, default='./save/MSATIS')
parser.add_argument('--load_dir', '-ld', type=str, default=None)
parser.add_argument('--log_dir', '-lod', type=str, default='./log/MSATIS')
parser.add_argument('--log_name', '-ln', type=str, default='log.txt')
parser.add_argument("--random_seed", '-rs', help='random seed', type=int, default=8682)
parser.add_argument("--fitlog", '-fl', help='whether uses fitlog', type=int, default=0)
#parser.add_argument('--gpu', '-g', action='store_true', help='use gpu', required=False, default=False)

# Training parameters.
parser.add_argument('--num_epoch', '-ne', type=int, default=5)
parser.add_argument('--batch_size', '-bs', type=int, default=16)
parser.add_argument('--l2', '-l2', type=float, default=1e-6)
parser.add_argument("--learning_rate", '-lr', type=float, default=0.001)
parser.add_argument('--dropout_rate', '-dr', type=float, default=0.5)
parser.add_argument('--gat_dropout_rate', '-gdr', type=float, default=0.5)
parser.add_argument('--threshold', '-thr', type=float, default=0.5)
parser.add_argument("--row_normalized", "-rn", action='store_true', help="row normalized for Adjacency matrix",
                    required=False, default=True)
parser.add_argument('--early_stop', action='store_true', default=False)
parser.add_argument('--patience', '-pa', type=int, default=10)

# Model parameters.
parser.add_argument('--intent_slot_loss_alpha', '-isalpha', type=float, default=0.9)
parser.add_argument('--intent_margin_loss_alpha', '-imalpha', type=float, default=1e-6)
parser.add_argument('--slot_margin_loss_alpha', '-smalpha', type=float, default=1.0)

parser.add_argument('--n_heads', '-nh', type=int, default=4, help='Number of attention heads.')
parser.add_argument('--alpha', '-alpha', type=float, default=0.2, help='Alpha for the leaky_relu.')
parser.add_argument('--step_num', '-sn', type=int, default=1, help='Step Number of HGAT.')
parser.add_argument('--n_layers_decoder_global', '-nl', type=int, default=2,help='gat layer Number of HGAT.')
parser.add_argument('--slot_graph_window', '-sgw', type=int, default=2)

parser.add_argument('--word_embedding_dim', '-wed', type=int, default=256)
parser.add_argument('--encoder_hidden_dim', '-ehd', type=int, default=256)
parser.add_argument('--attention_output_dim', '-aod', type=int, default=256)
parser.add_argument('--attention_hidden_dim', '-ahd', type=int, default=2048)
parser.add_argument('--decoder_hidden_dim', '-dhd', type=int, default=256)
parser.add_argument('--decoder_gat_hidden_dim', '-dghd', type=int, default=128)
args = parser.parse_args()
args.gpu = torch.cuda.is_available()
print(str(vars(args)))
