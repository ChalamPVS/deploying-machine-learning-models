import pandas as pd
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline

from regression_model.config import config
<<<<<<< HEAD
from regression_model import __version__ as _version

import logging
import typing as t


_logger = logging.getLogger(__name__)
=======
from regression_model.config import logging_config
from regression_model import __version__ as _version

_logger = logging_config.get_logger(__name__)
>>>>>>> 6162c318b58b225e0061fccd6c64cd67fe205c1b


def load_dataset(*, file_name: str
                 ) -> pd.DataFrame:
    _data = pd.read_csv(f'{config.DATASET_DIR}/{file_name}')
    return _data


def save_pipeline(*, pipeline_to_persist) -> None:
    """Persist the pipeline.
<<<<<<< HEAD

    Saves the versioned model, and overwrites any previous
    saved models. This ensures that when the package is
    published, there is only one trained model that can be
    called, and we know exactly how it was built.
    """

=======

    Saves the versioned model, and overwrites any previous
    saved models. This ensures that when the package is
    published, there is only one trained model that can be
    called, and we know exactly how it was built.
    """

>>>>>>> 6162c318b58b225e0061fccd6c64cd67fe205c1b
    # Prepare versioned save file name
    save_file_name = f'{config.PIPELINE_SAVE_FILE}{_version}.pkl'
    save_path = config.TRAINED_MODEL_DIR / save_file_name

    remove_old_pipelines(files_to_keep=[save_file_name])
    joblib.dump(pipeline_to_persist, save_path)
    _logger.info(f'saved pipeline: {save_file_name}')


def load_pipeline(*, file_name: str
                  ) -> Pipeline:
    """Load a persisted pipeline."""

    file_path = config.TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model


def remove_old_pipelines(*, files_to_keep: t.List[str]) -> None:
    """
    Remove old model pipelines.

    This is to ensure there is a simple one-to-one
    mapping between the package version and the model
    version to be imported and used by other applications.
    However, we do also include the immediate previous
    pipeline version for differential testing purposes.
    """
    do_not_delete = files_to_keep + ['__init__.py']
    for model_file in config.TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            model_file.unlink()
