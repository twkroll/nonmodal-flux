import importlib

import jax
import jax.numpy as jnp


def test_package_imports() -> None:
    module = importlib.import_module("nonmodal_flux")
    assert module.__version__ == "0.0.1"


def test_jax_x64_can_be_enabled() -> None:
    jax.config.update("jax_enable_x64", True)
    value = jnp.asarray([1.0], dtype=jnp.float64)
    assert value.dtype == jnp.float64
