"""
Script to insert model training metrics
to the tensorflow tensorboard
"""
from torch.utils.tensorboard import SummaryWriter
class TfLogWriter:
    """
    Log metrics to tensorboard
    and calculate training time
    """
    def __init__(self):
        self.tboard = None

    def begin_run(self, run):
        """
        :param run: run containing custom param
        write to tensorboard
        """
        self.tboard = SummaryWriter(comment=f'-{run.models.__class__.__name__ + str(run.batch_size)}')

    def add_to_board(self, train_loss, test_loss, num_epoch):
        """
        :param train_loss: epoch training loss
        :param test_loss: epoch validation loss
        :param num_epoch: the number of the current epoch
        :return:  Record epoch and losses  to TensorBoard
        """
        self.tboard.add_scalar('Test Loss', test_loss, num_epoch)
        self.tboard.add_scalar('Train Loss', train_loss, num_epoch)
