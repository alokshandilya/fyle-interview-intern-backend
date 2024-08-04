from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.assignments.student import submit_assignment
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentSchema
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)


@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_principal_assignments(p):
    """Returns list of assignments"""
    submitted_and_graded_assignments = Assignment.get_submitted_and_graded_assignments()
    submitted_and_graded_assignments_dump = AssignmentSchema().dump(submitted_and_graded_assignments, many=True)
    return APIResponse.respond(data=submitted_and_graded_assignments_dump)

