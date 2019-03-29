# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class FaceOperations(object):
    """FaceOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def find_similar(
            self, face_id, face_list_id=None, large_face_list_id=None, face_ids=None, max_num_of_candidates_returned=20, mode="matchPerson", custom_headers=None, raw=False, **operation_config):
        """Given query face's faceId, to search the similar-looking faces from a
        faceId array, a face list or a large face list. faceId array contains
        the faces created by [Face -
        Detect](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236),
        which will expire 24 hours after creation. A "faceListId" is created by
        [FaceList -
        Create](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039524b)
        containing persistedFaceIds that will not expire. And a
        "largeFaceListId" is created by [LargeFaceList -
        Create](/docs/services/563879b61984550e40cbbe8d/operations/5a157b68d2de3616c086f2cc)
        containing persistedFaceIds that will also not expire. Depending on the
        input the returned similar faces list contains faceIds or
        persistedFaceIds ranked by similarity.
        <br/>Find similar has two working modes, "matchPerson" and "matchFace".
        "matchPerson" is the default mode that it tries to find faces of the
        same person as possible by using internal same-person thresholds. It is
        useful to find a known person's other photos. Note that an empty list
        will be returned if no faces pass the internal thresholds. "matchFace"
        mode ignores same-person thresholds and returns ranked similar faces
        anyway, even the similarity is low. It can be used in the cases like
        searching celebrity-looking faces.
        <br/>The 'recognitionModel' associated with the query face's faceId
        should be the same as the 'recognitionModel' used by the target faceId
        array, face list or large face list.
        .

        :param face_id: FaceId of the query face. User needs to call Face -
         Detect first to get a valid faceId. Note that this faceId is not
         persisted and will expire 24 hours after the detection call
        :type face_id: str
        :param face_list_id: An existing user-specified unique candidate face
         list, created in Face List - Create a Face List. Face list contains a
         set of persistedFaceIds which are persisted and will never expire.
         Parameter faceListId, largeFaceListId and faceIds should not be
         provided at the same time.
        :type face_list_id: str
        :param large_face_list_id: An existing user-specified unique candidate
         large face list, created in LargeFaceList - Create. Large face list
         contains a set of persistedFaceIds which are persisted and will never
         expire. Parameter faceListId, largeFaceListId and faceIds should not
         be provided at the same time.
        :type large_face_list_id: str
        :param face_ids: An array of candidate faceIds. All of them are
         created by Face - Detect and the faceIds will expire 24 hours after
         the detection call. The number of faceIds is limited to 1000.
         Parameter faceListId, largeFaceListId and faceIds should not be
         provided at the same time.
        :type face_ids: list[str]
        :param max_num_of_candidates_returned: The number of top similar faces
         returned. The valid range is [1, 1000].
        :type max_num_of_candidates_returned: int
        :param mode: Similar face searching mode. It can be "matchPerson" or
         "matchFace". Possible values include: 'matchPerson', 'matchFace'
        :type mode: str or
         ~azure.cognitiveservices.vision.face.models.FindSimilarMatchMode
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~azure.cognitiveservices.vision.face.models.SimilarFace]
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        body = models.FindSimilarRequest(face_id=face_id, face_list_id=face_list_id, large_face_list_id=large_face_list_id, face_ids=face_ids, max_num_of_candidates_returned=max_num_of_candidates_returned, mode=mode)

        # Construct URL
        url = self.find_similar.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'FindSimilarRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[SimilarFace]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    find_similar.metadata = {'url': '/findsimilars'}

    def group(
            self, face_ids, custom_headers=None, raw=False, **operation_config):
        """Divide candidate faces into groups based on face similarity.<br />
        * The output is one or more disjointed face groups and a messyGroup. A
        face group contains faces that have similar looking, often of the same
        person. Face groups are ranked by group size, i.e. number of faces.
        Notice that faces belonging to a same person might be split into
        several groups in the result.
        * MessyGroup is a special face group containing faces that cannot find
        any similar counterpart face from original faces. The messyGroup will
        not appear in the result if all faces found their counterparts.
        * Group API needs at least 2 candidate faces and 1000 at most. We
        suggest to try [Face -
        Verify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523a)
        when you only have 2 candidate faces.
        * The 'recognitionModel' associated with the query faces' faceIds
        should be the same.
        .

        :param face_ids: Array of candidate faceId created by Face - Detect.
         The maximum is 1000 faces
        :type face_ids: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: GroupResult or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.face.models.GroupResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        body = models.GroupRequest(face_ids=face_ids)

        # Construct URL
        url = self.group.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'GroupRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('GroupResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    group.metadata = {'url': '/group'}

    def identify(
            self, face_ids, person_group_id=None, large_person_group_id=None, max_num_of_candidates_returned=1, confidence_threshold=None, custom_headers=None, raw=False, **operation_config):
        """1-to-many identification to find the closest matches of the specific
        query person face from a person group or large person group.
        <br/> For each face in the faceIds array, Face Identify will compute
        similarities between the query face and all the faces in the person
        group (given by personGroupId) or large person group (given by
        largePersonGroupId), and return candidate person(s) for that face
        ranked by similarity confidence. The person group/large person group
        should be trained to make it ready for identification. See more in
        [PersonGroup -
        Train](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395249)
        and [LargePersonGroup -
        Train](/docs/services/563879b61984550e40cbbe8d/operations/599ae2d16ac60f11b48b5aa4).
        <br/>
        Remarks:<br />
        * The algorithm allows more than one face to be identified
        independently at the same request, but no more than 10 faces.
        * Each person in the person group/large person group could have more
        than one face, but no more than 248 faces.
        * Higher face image quality means better identification precision.
        Please consider high-quality faces: frontal, clear, and face size is
        200x200 pixels (100 pixels between eyes) or bigger.
        * Number of candidates returned is restricted by
        maxNumOfCandidatesReturned and confidenceThreshold. If no person is
        identified, the returned candidates will be an empty array.
        * Try [Face - Find
        Similar](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395237)
        when you need to find similar faces from a face list/large face list
        instead of a person group/large person group.
        * The 'recognitionModel' associated with the query faces' faceIds
        should be the same as the 'recognitionModel' used by the target person
        group or large person group.
        .

        :param face_ids: Array of query faces faceIds, created by the Face -
         Detect. Each of the faces are identified independently. The valid
         number of faceIds is between [1, 10].
        :type face_ids: list[str]
        :param person_group_id: PersonGroupId of the target person group,
         created by PersonGroup - Create. Parameter personGroupId and
         largePersonGroupId should not be provided at the same time.
        :type person_group_id: str
        :param large_person_group_id: LargePersonGroupId of the target large
         person group, created by LargePersonGroup - Create. Parameter
         personGroupId and largePersonGroupId should not be provided at the
         same time.
        :type large_person_group_id: str
        :param max_num_of_candidates_returned: The range of
         maxNumOfCandidatesReturned is between 1 and 5 (default is 1).
        :type max_num_of_candidates_returned: int
        :param confidence_threshold: Confidence threshold of identification,
         used to judge whether one face belong to one person. The range of
         confidenceThreshold is [0, 1] (default specified by algorithm).
        :type confidence_threshold: float
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype:
         list[~azure.cognitiveservices.vision.face.models.IdentifyResult] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        body = models.IdentifyRequest(face_ids=face_ids, person_group_id=person_group_id, large_person_group_id=large_person_group_id, max_num_of_candidates_returned=max_num_of_candidates_returned, confidence_threshold=confidence_threshold)

        # Construct URL
        url = self.identify.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'IdentifyRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[IdentifyResult]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    identify.metadata = {'url': '/identify'}

    def verify_face_to_face(
            self, face_id1, face_id2, custom_headers=None, raw=False, **operation_config):
        """Verify whether two faces belong to a same person or whether one face
        belongs to a person.
        <br/>
        Remarks:<br />
        * Higher face image quality means better identification precision.
        Please consider high-quality faces: frontal, clear, and face size is
        200x200 pixels (100 pixels between eyes) or bigger.
        * For the scenarios that are sensitive to accuracy please make your own
        judgment.
        * The 'recognitionModel' associated with the query faces' faceIds
        should be the same as the 'recognitionModel' used by the target face,
        person group or large person group.
        .

        :param face_id1: FaceId of the first face, comes from Face - Detect
        :type face_id1: str
        :param face_id2: FaceId of the second face, comes from Face - Detect
        :type face_id2: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VerifyResult or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.face.models.VerifyResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        body = models.VerifyFaceToFaceRequest(face_id1=face_id1, face_id2=face_id2)

        # Construct URL
        url = self.verify_face_to_face.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'VerifyFaceToFaceRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VerifyResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    verify_face_to_face.metadata = {'url': '/verify'}

    def detect_with_url(
            self, url, return_face_id=True, return_face_landmarks=False, return_face_attributes=None, recognition_model="recognition_01", return_recognition_model=False, custom_headers=None, raw=False, **operation_config):
        """Detect human faces in an image, return face rectangles, and optionally
        with faceIds, landmarks, and attributes.<br />
        * Optional parameters including faceId, landmarks, and attributes.
        Attributes include age, gender, headPose, smile, facialHair, glasses,
        emotion, hair, makeup, occlusion, accessories, blur, exposure and
        noise.
        * The extracted face feature, instead of the actual image, will be
        stored on server. The faceId is an identifier of the face feature and
        will be used in [Face -
        Identify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395239),
        [Face -
        Verify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f3039523a),
        and [Face - Find
        Similar](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395237).
        It will expire 24 hours after the detection call.
        * Higher face image quality means better detection and recognition
        precision. Please consider high-quality faces: frontal, clear, and face
        size is 200x200 pixels (100 pixels between eyes) or bigger.
        * JPEG, PNG, GIF (the first frame), and BMP format are supported. The
        allowed image file size is from 1KB to 6MB.
        * Faces are detectable when its size is 36x36 to 4096x4096 pixels. If
        need to detect very small but clear faces, please try to enlarge the
        input image.
        * Up to 64 faces can be returned for an image. Faces are ranked by face
        rectangle size from large to small.
        * Face detector prefer frontal and near-frontal faces. There are cases
        that faces may not be detected, e.g. exceptionally large face angles
        (head-pose) or being occluded, or wrong image orientation.
        * Attributes (age, gender, headPose, smile, facialHair, glasses,
        emotion, hair, makeup, occlusion, accessories, blur, exposure and
        noise) may not be perfectly accurate. HeadPose's pitch value is a
        reserved field and will always return 0.
        * Different 'recognitionModel' values are provided. If follow-up
        operations like Verify, Identify, Find Similar are needed, please
        specify the recognition model with 'recognitionModel' parameter. The
        default value for 'recognitionModel' is 'recognition_01', if latest
        model needed, please explicitly specify the model you need in this
        parameter. Once specified, the detected faceIds will be associated with
        the specified recognition model. More details, please refer to [How to
        specify a recognition
        model](https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/specify-recognition-model)
        .

        :param url: Publicly reachable URL of an image
        :type url: str
        :param return_face_id: A value indicating whether the operation should
         return faceIds of detected faces.
        :type return_face_id: bool
        :param return_face_landmarks: A value indicating whether the operation
         should return landmarks of the detected faces.
        :type return_face_landmarks: bool
        :param return_face_attributes: Analyze and return the one or more
         specified face attributes in the comma-separated string like
         "returnFaceAttributes=age,gender". Supported face attributes include
         age, gender, headPose, smile, facialHair, glasses and emotion. Note
         that each face attribute analysis has additional computational and
         time cost.
        :type return_face_attributes: list[str or
         ~azure.cognitiveservices.vision.face.models.FaceAttributeType]
        :param recognition_model: Name of recognition model. Recognition model
         is used when the face features are extracted and associated with
         detected faceIds, (Large)FaceList or (Large)PersonGroup. A recognition
         model name can be provided when performing Face - Detect or
         (Large)FaceList - Create or (Large)PersonGroup - Create. The default
         value is 'recognition_01', if latest model needed, please explicitly
         specify the model you need. Possible values include: 'recognition_01',
         'recognition_02'
        :type recognition_model: str or
         ~azure.cognitiveservices.vision.face.models.RecognitionModel
        :param return_recognition_model: A value indicating whether the
         operation should return 'recognitionModel' in response.
        :type return_recognition_model: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~azure.cognitiveservices.vision.face.models.DetectedFace]
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        image_url = models.ImageUrl(url=url)

        # Construct URL
        url = self.detect_with_url.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if return_face_id is not None:
            query_parameters['returnFaceId'] = self._serialize.query("return_face_id", return_face_id, 'bool')
        if return_face_landmarks is not None:
            query_parameters['returnFaceLandmarks'] = self._serialize.query("return_face_landmarks", return_face_landmarks, 'bool')
        if return_face_attributes is not None:
            query_parameters['returnFaceAttributes'] = self._serialize.query("return_face_attributes", return_face_attributes, '[FaceAttributeType]', div=',')
        if recognition_model is not None:
            query_parameters['recognitionModel'] = self._serialize.query("recognition_model", recognition_model, 'str')
        if return_recognition_model is not None:
            query_parameters['returnRecognitionModel'] = self._serialize.query("return_recognition_model", return_recognition_model, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(image_url, 'ImageUrl')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[DetectedFace]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    detect_with_url.metadata = {'url': '/detect'}

    def verify_face_to_person(
            self, face_id, person_id, person_group_id=None, large_person_group_id=None, custom_headers=None, raw=False, **operation_config):
        """Verify whether two faces belong to a same person. Compares a face Id
        with a Person Id.

        :param face_id: FaceId of the face, comes from Face - Detect
        :type face_id: str
        :param person_id: Specify a certain person in a person group or a
         large person group. personId is created in PersonGroup Person - Create
         or LargePersonGroup Person - Create.
        :type person_id: str
        :param person_group_id: Using existing personGroupId and personId for
         fast loading a specified person. personGroupId is created in
         PersonGroup - Create. Parameter personGroupId and largePersonGroupId
         should not be provided at the same time.
        :type person_group_id: str
        :param large_person_group_id: Using existing largePersonGroupId and
         personId for fast loading a specified person. largePersonGroupId is
         created in LargePersonGroup - Create. Parameter personGroupId and
         largePersonGroupId should not be provided at the same time.
        :type large_person_group_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VerifyResult or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.face.models.VerifyResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        body = models.VerifyFaceToPersonRequest(face_id=face_id, person_group_id=person_group_id, large_person_group_id=large_person_group_id, person_id=person_id)

        # Construct URL
        url = self.verify_face_to_person.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'VerifyFaceToPersonRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VerifyResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    verify_face_to_person.metadata = {'url': '/verify'}

    def detect_with_stream(
            self, image, return_face_id=True, return_face_landmarks=False, return_face_attributes=None, recognition_model="recognition_01", return_recognition_model=False, custom_headers=None, raw=False, callback=None, **operation_config):
        """Detect human faces in an image and returns face locations, and
        optionally with faceIds, landmarks, and attributes.

        :param image: An image stream.
        :type image: Generator
        :param return_face_id: A value indicating whether the operation should
         return faceIds of detected faces.
        :type return_face_id: bool
        :param return_face_landmarks: A value indicating whether the operation
         should return landmarks of the detected faces.
        :type return_face_landmarks: bool
        :param return_face_attributes: Analyze and return the one or more
         specified face attributes in the comma-separated string like
         "returnFaceAttributes=age,gender". Supported face attributes include
         age, gender, headPose, smile, facialHair, glasses and emotion. Note
         that each face attribute analysis has additional computational and
         time cost.
        :type return_face_attributes: list[str or
         ~azure.cognitiveservices.vision.face.models.FaceAttributeType]
        :param recognition_model: Name of recognition model. Recognition model
         is used when the face features are extracted and associated with
         detected faceIds, (Large)FaceList or (Large)PersonGroup. A recognition
         model name can be provided when performing Face - Detect or
         (Large)FaceList - Create or (Large)PersonGroup - Create. The default
         value is 'recognition_01', if latest model needed, please explicitly
         specify the model you need. Possible values include: 'recognition_01',
         'recognition_02'
        :type recognition_model: str or
         ~azure.cognitiveservices.vision.face.models.RecognitionModel
        :param return_recognition_model: A value indicating whether the
         operation should return 'recognitionModel' in response.
        :type return_recognition_model: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~azure.cognitiveservices.vision.face.models.DetectedFace]
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = self.detect_with_stream.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if return_face_id is not None:
            query_parameters['returnFaceId'] = self._serialize.query("return_face_id", return_face_id, 'bool')
        if return_face_landmarks is not None:
            query_parameters['returnFaceLandmarks'] = self._serialize.query("return_face_landmarks", return_face_landmarks, 'bool')
        if return_face_attributes is not None:
            query_parameters['returnFaceAttributes'] = self._serialize.query("return_face_attributes", return_face_attributes, '[FaceAttributeType]', div=',')
        if recognition_model is not None:
            query_parameters['recognitionModel'] = self._serialize.query("recognition_model", recognition_model, 'str')
        if return_recognition_model is not None:
            query_parameters['returnRecognitionModel'] = self._serialize.query("return_recognition_model", return_recognition_model, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/octet-stream'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._client.stream_upload(image, callback)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[DetectedFace]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    detect_with_stream.metadata = {'url': '/detect'}
