import numpy as np
import pandas as pd

from regression_model.processing.data_management import load_pipeline
from regression_model.config import config
from regression_model.processing.validation import validate_inputs
<<<<<<< HEAD
=======
from regression_model.config.logging_config import get_logger
>>>>>>> 6162c318b58b225e0061fccd6c64cd67fe205c1b
from regression_model import __version__ as _version

import logging
import typing as t

<<<<<<< HEAD

_logger = logging.getLogger(__name__)
=======
_logger = get_logger(logger_name=__name__)
>>>>>>> 6162c318b58b225e0061fccd6c64cd67fe205c1b

pipeline_file_name = f'{config.PIPELINE_SAVE_FILE}{_version}.pkl'
_price_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data: t.Union[pd.DataFrame, dict],
                    ) -> dict:
    """Make a prediction using a saved model pipeline.

    Args:
        input_data: Array of model prediction inputs.

    Returns:
        Predictions for each input row, as well as the model version.
    """

    data = pd.DataFrame(input_data)
    validated_data = validate_inputs(input_data=data)

    prediction = _price_pipe.predict(validated_data[config.FEATURES])

    output = np.exp(prediction)

    results = {'predictions': output, 'version': _version}

    _logger.info(
        f'Making predictions with model version: {_version} '
        f'Inputs: {validated_data} '
        f'Predictions: {results}')

    return results
