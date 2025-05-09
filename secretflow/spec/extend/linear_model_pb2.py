# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: secretflow/spec/extend/linear_model.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)secretflow/spec/extend/linear_model.proto\x12\x16secretflow.spec.extend\"L\n\rFeatureWeight\x12\x14\n\x0c\x66\x65\x61ture_name\x18\x01 \x01(\t\x12\r\n\x05party\x18\x02 \x01(\t\x12\x16\n\x0e\x66\x65\x61ture_weight\x18\x03 \x01(\x02\"o\n\x0bLinearModel\x12>\n\x0f\x66\x65\x61ture_weights\x18\x01 \x03(\x0b\x32%.secretflow.spec.extend.FeatureWeight\x12\x0c\n\x04\x62ias\x18\x02 \x01(\x02\x12\x12\n\nmodel_hash\x18\x03 \x01(\t\"\x8d\x02\n\nPublicInfo\x12\x0c\n\x04link\x18\x01 \x01(\t\x12\x0f\n\x07y_scale\x18\x02 \x01(\x01\x12\x12\n\noffset_col\x18\x03 \x01(\t\x12\x11\n\tlabel_col\x18\x04 \x01(\t\x12\x14\n\x0c\x66xp_exp_mode\x18\x05 \x01(\x05\x12\x15\n\rfxp_exp_iters\x18\x06 \x01(\x05\x12%\n\x1d\x65xperimental_exp_prime_offset\x18\x07 \x01(\r\x12\x32\n*experimental_exp_prime_disable_lower_bound\x18\x08 \x01(\x08\x12\x31\n)experimental_exp_prime_enable_upper_bound\x18\t \x01(\x08\"\x85\x01\n\x16GeneralizedLinearModel\x12\x37\n\x0bpublic_info\x18\x01 \x01(\x0b\x32\".secretflow.spec.extend.PublicInfo\x12\x32\n\x05model\x18\x02 \x01(\x0b\x32#.secretflow.spec.extend.LinearModelB\x1c\n\x1aorg.secretflow.spec.extendb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'secretflow.spec.extend.linear_model_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032org.secretflow.spec.extend'
  _FEATUREWEIGHT._serialized_start=69
  _FEATUREWEIGHT._serialized_end=145
  _LINEARMODEL._serialized_start=147
  _LINEARMODEL._serialized_end=258
  _PUBLICINFO._serialized_start=261
  _PUBLICINFO._serialized_end=530
  _GENERALIZEDLINEARMODEL._serialized_start=533
  _GENERALIZEDLINEARMODEL._serialized_end=666
# @@protoc_insertion_point(module_scope)
