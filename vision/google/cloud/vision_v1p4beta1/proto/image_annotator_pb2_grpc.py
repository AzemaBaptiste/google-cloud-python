# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.vision_v1p4beta1.proto import (
    image_annotator_pb2 as google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_image__annotator__pb2,
)
from google.longrunning import (
    operations_pb2 as google_dot_longrunning_dot_operations__pb2,
)


class ImageAnnotatorStub(object):
    """Service that performs Google Cloud Vision API detection tasks over client
  images, such as face, landmark, logo, label, and text detection. The
  ImageAnnotator service returns detected entities from the images.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.BatchAnnotateImages = channel.unary_unary(
            "/google.cloud.vision.v1p4beta1.ImageAnnotator/BatchAnnotateImages",
            request_serializer=google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_image__annotator__pb2.BatchAnnotateImagesRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_image__annotator__pb2.BatchAnnotateImagesResponse.FromString,
        )
        self.BatchAnnotateFiles = channel.unary_unary(
            "/google.cloud.vision.v1p4beta1.ImageAnnotator/BatchAnnotateFiles",
            request_serializer=google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_image__annotator__pb2.BatchAnnotateFilesRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_image__annotator__pb2.BatchAnnotateFilesResponse.FromString,
        )
        self.AsyncBatchAnnotateImages = channel.unary_unary(
            "/google.cloud.vision.v1p4beta1.ImageAnnotator/AsyncBatchAnnotateImages",
            request_serializer=google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_image__annotator__pb2.AsyncBatchAnnotateImagesRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.AsyncBatchAnnotateFiles = channel.unary_unary(
            "/google.cloud.vision.v1p4beta1.ImageAnnotator/AsyncBatchAnnotateFiles",
            request_serializer=google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_image__annotator__pb2.AsyncBatchAnnotateFilesRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )


class ImageAnnotatorServicer(object):
    """Service that performs Google Cloud Vision API detection tasks over client
  images, such as face, landmark, logo, label, and text detection. The
  ImageAnnotator service returns detected entities from the images.
  """

    def BatchAnnotateImages(self, request, context):
        """Run image detection and annotation for a batch of images.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BatchAnnotateFiles(self, request, context):
        """Service that performs image detection and annotation for a batch of files.
    Now only "application/pdf", "image/tiff" and "image/gif" are supported.

    This service will extract at most 5 (customers can specify which 5 in
    AnnotateFileRequest.pages) frames (gif) or pages (pdf or tiff) from each
    file provided and perform detection and annotation for each image
    extracted.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AsyncBatchAnnotateImages(self, request, context):
        """Run asynchronous image detection and annotation for a list of images.

    Progress and results can be retrieved through the
    `google.longrunning.Operations` interface.
    `Operation.metadata` contains `OperationMetadata` (metadata).
    `Operation.response` contains `AsyncBatchAnnotateImagesResponse` (results).

    This service will write image annotation outputs to json files in customer
    GCS bucket, each json file containing BatchAnnotateImagesResponse proto.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AsyncBatchAnnotateFiles(self, request, context):
        """Run asynchronous image detection and annotation for a list of generic
    files, such as PDF files, which may contain multiple pages and multiple
    images per page. Progress and results can be retrieved through the
    `google.longrunning.Operations` interface.
    `Operation.metadata` contains `OperationMetadata` (metadata).
    `Operation.response` contains `AsyncBatchAnnotateFilesResponse` (results).
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ImageAnnotatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "BatchAnnotateImages": grpc.unary_unary_rpc_method_handler(
            servicer.BatchAnnotateImages,
            request_deserializer=google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_image__annotator__pb2.BatchAnnotateImagesRequest.FromString,
            response_serializer=google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_image__annotator__pb2.BatchAnnotateImagesResponse.SerializeToString,
        ),
        "BatchAnnotateFiles": grpc.unary_unary_rpc_method_handler(
            servicer.BatchAnnotateFiles,
            request_deserializer=google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_image__annotator__pb2.BatchAnnotateFilesRequest.FromString,
            response_serializer=google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_image__annotator__pb2.BatchAnnotateFilesResponse.SerializeToString,
        ),
        "AsyncBatchAnnotateImages": grpc.unary_unary_rpc_method_handler(
            servicer.AsyncBatchAnnotateImages,
            request_deserializer=google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_image__annotator__pb2.AsyncBatchAnnotateImagesRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "AsyncBatchAnnotateFiles": grpc.unary_unary_rpc_method_handler(
            servicer.AsyncBatchAnnotateFiles,
            request_deserializer=google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_image__annotator__pb2.AsyncBatchAnnotateFilesRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.vision.v1p4beta1.ImageAnnotator", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
