# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from yandex.cloud.ai.translate.v2 import translation_service_pb2 as yandex_dot_cloud_dot_ai_dot_translate_dot_v2_dot_translation__service__pb2


class TranslationServiceStub(object):
  """A set of methods for the Yandex Translate service.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Translate = channel.unary_unary(
        '/yandex.cloud.ai.translate.v2.TranslationService/Translate',
        request_serializer=yandex_dot_cloud_dot_ai_dot_translate_dot_v2_dot_translation__service__pb2.TranslateRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_ai_dot_translate_dot_v2_dot_translation__service__pb2.TranslateResponse.FromString,
        )
    self.DetectLanguage = channel.unary_unary(
        '/yandex.cloud.ai.translate.v2.TranslationService/DetectLanguage',
        request_serializer=yandex_dot_cloud_dot_ai_dot_translate_dot_v2_dot_translation__service__pb2.DetectLanguageRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_ai_dot_translate_dot_v2_dot_translation__service__pb2.DetectLanguageResponse.FromString,
        )
    self.ListLanguages = channel.unary_unary(
        '/yandex.cloud.ai.translate.v2.TranslationService/ListLanguages',
        request_serializer=yandex_dot_cloud_dot_ai_dot_translate_dot_v2_dot_translation__service__pb2.ListLanguagesRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_ai_dot_translate_dot_v2_dot_translation__service__pb2.ListLanguagesResponse.FromString,
        )


class TranslationServiceServicer(object):
  """A set of methods for the Yandex Translate service.
  """

  def Translate(self, request, context):
    """Translates the text to the specified language.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DetectLanguage(self, request, context):
    """Detects the language of the text.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListLanguages(self, request, context):
    """Retrieves the list of supported languages.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TranslationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Translate': grpc.unary_unary_rpc_method_handler(
          servicer.Translate,
          request_deserializer=yandex_dot_cloud_dot_ai_dot_translate_dot_v2_dot_translation__service__pb2.TranslateRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_ai_dot_translate_dot_v2_dot_translation__service__pb2.TranslateResponse.SerializeToString,
      ),
      'DetectLanguage': grpc.unary_unary_rpc_method_handler(
          servicer.DetectLanguage,
          request_deserializer=yandex_dot_cloud_dot_ai_dot_translate_dot_v2_dot_translation__service__pb2.DetectLanguageRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_ai_dot_translate_dot_v2_dot_translation__service__pb2.DetectLanguageResponse.SerializeToString,
      ),
      'ListLanguages': grpc.unary_unary_rpc_method_handler(
          servicer.ListLanguages,
          request_deserializer=yandex_dot_cloud_dot_ai_dot_translate_dot_v2_dot_translation__service__pb2.ListLanguagesRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_ai_dot_translate_dot_v2_dot_translation__service__pb2.ListLanguagesResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'yandex.cloud.ai.translate.v2.TranslationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
