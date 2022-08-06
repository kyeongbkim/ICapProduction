import pdb
import sys
import collections

iCap = None

def load_pretrained_model(dataset="Flickr30k", model='transformer', epochs=30, deployment=True):
    if model == 'cascade':
        import cascaded_encoder_decoder
        iCap = cascaded_encoder_decoder.ImageCaptioningWithCascadedEncoderDecoder(dataset, deployment=deployment)
    elif model == 'merge':
        import merged_encoder_decoder
        iCap = merged_encoder_decoder.ImageCaptioningWithMergedEncoderDecoder(dataset, deployment=deployment)
    elif model == 'attention':
        import attention
        iCap = attention.ImageCaptioningWithAttention(dataset, deployment=deployment)
    elif model == 'transformer':
        import transformer
        iCap = transformer.ImageCaptioningWithTransformer(dataset, deployment=deployment)
    else:
        assert False, 'Unknown model {}'.format(model)

    iCap.load_weights(epochs)
    return iCap

def predict(file_path):
    return iCap.predict(file_path=file_path)

def init(dataset="Flickr30k", model='transformer', epochs=30):
    global iCap
    iCap = load_pretrained_model(dataset=dataset, model=model, epochs=epochs, deployment=True)

