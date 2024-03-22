import tensorflow as tf

if __name__ == '__main__':
    model = tf.keras.models.load_model('unet_model')
    # plot the model architecture on a tensorboard color image and beautiful to see the V unet model
    # do it beutifully and colorfully and to see it as a V unet model
    tf.keras.utils.plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True)
