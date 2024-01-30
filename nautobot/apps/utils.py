"""Nautobot utility functions."""

from nautobot.core.releases import get_latest_release
from nautobot.core.utils.color import foreground_color, hex_to_rgb, lighten_color, rgb_to_hex
from nautobot.core.utils.config import get_settings_or_config
from nautobot.core.utils.data import (
    deepmerge,
    flatten_dict,
    flatten_iterable,
    is_url,
    is_uuid,
    merge_dicts_without_collision,
    render_jinja2,
    shallow_compare_dict,
    to_meters,
)
from nautobot.core.utils.deprecation import class_deprecated, class_deprecated_in_favor_of
from nautobot.core.utils.filtering import (
    build_lookup_label,
    get_all_lookup_expr_for_field,
    get_filter_field_label,
    get_filterset_field,
    get_filterset_parameter_form_field,
)
from nautobot.core.utils.git import BranchDoesNotExist, convert_git_diff_log_to_list, GitRepo, swap_status_initials
from nautobot.core.utils.logging import sanitize
from nautobot.core.utils.lookup import (
    get_changes_for_model,
    get_filterset_for_model,
    get_form_for_model,
    get_model_from_name,
    get_related_class_for_model,
    get_route_for_model,
    get_table_for_model,
)
from nautobot.core.utils.navigation import (
    get_all_new_ui_ready_routes,
    get_only_new_ui_ready_routes,
    is_route_new_ui_ready,
)
from nautobot.core.utils.permissions import (
    get_permission_for_model,
    permission_is_exempt,
    resolve_permission,
    resolve_permission_ct,
)
from nautobot.core.utils.requests import (
    convert_querydict_to_factory_formset_acceptable_querydict,
    ensure_content_type_and_field_name_in_query_params,
    get_filterable_params_from_filter_params,
    is_single_choice_field,
    normalize_querydict,
)
from nautobot.extras.plugins.validators import custom_validator_clean, wrap_model_clean_methods
from nautobot.extras.utils import (
    ChangeLoggedModelsQuery,
    check_if_key_is_graphql_safe,
    FeaturedQueryMixin,
    FeatureQuery,
    fixup_null_statuses,
    generate_signature,
    get_base_template,
    get_celery_queues,
    get_worker_count,
    image_upload,
    migrate_role_data,
    populate_model_features_registry,
    refresh_job_model_from_job_class,
    remove_prefix_from_cf_key,
    RoleModelsQuery,
    TaggableClassesQuery,
    task_queues_as_choices,
)

__all__ = (
    "BranchDoesNotExist",
    "build_lookup_label",
    "ChangeLoggedModelsQuery",
    "check_if_key_is_graphql_safe",
    "class_deprecated",
    "class_deprecated_in_favor_of",
    "convert_git_diff_log_to_list",
    "convert_querydict_to_factory_formset_acceptable_querydict",
    "custom_validator_clean",
    "deepmerge",
    "ensure_content_type_and_field_name_in_query_params",
    "FeaturedQueryMixin",
    "FeatureQuery",
    "fixup_null_statuses",
    "flatten_dict",
    "flatten_iterable",
    "foreground_color",
    "generate_signature",
    "get_all_lookup_expr_for_field",
    "get_all_new_ui_ready_routes",
    "get_base_template",
    "get_celery_queues",
    "get_changes_for_model",
    "get_filter_field_label",
    "get_filterable_params_from_filter_params",
    "get_filterset_field",
    "get_filterset_for_model",
    "get_filterset_parameter_form_field",
    "get_form_for_model",
    "get_latest_release",
    "get_model_from_name",
    "get_only_new_ui_ready_routes",
    "get_permission_for_model",
    "get_related_class_for_model",
    "get_route_for_model",
    "get_settings_or_config",
    "get_table_for_model",
    "get_worker_count",
    "GitRepo",
    "hex_to_rgb",
    "image_upload",
    "is_route_new_ui_ready",
    "is_single_choice_field",
    "is_url",
    "is_uuid",
    "lighten_color",
    "merge_dicts_without_collision",
    "migrate_role_data",
    "normalize_querydict",
    "permission_is_exempt",
    "populate_model_features_registry",
    "refresh_job_model_from_job_class",
    "remove_prefix_from_cf_key",
    "render_jinja2",
    "resolve_permission",
    "resolve_permission_ct",
    "rgb_to_hex",
    "RoleModelsQuery",
    "sanitize",
    "shallow_compare_dict",
    "swap_status_initials",
    "TaggableClassesQuery",
    "task_queues_as_choices",
    "to_meters",
    "wrap_model_clean_methods",
)
