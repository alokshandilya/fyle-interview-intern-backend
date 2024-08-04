from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment, AssignmentStateEnum
from core.models.teachers import Teacher

from .schema import AssignmentSchema, AssignmentGradeSchema, TeacherSchema
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)


@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_principal_assignments(p):
    """Returns list of assignments"""
    submitted_and_graded_assignments = Assignment.get_submitted_and_graded_assignments()
    submitted_and_graded_assignments_dump = AssignmentSchema().dump(submitted_and_graded_assignments, many=True)
    return APIResponse.respond(data=submitted_and_graded_assignments_dump)


# @principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
# @decorators.authenticate_principal
# def list_teachers(p):
#     """Returns list of all teachers"""
#     all_teachers = Teacher.get_all_teachers()
#     all_teachers_dump = TeacherSchema().dump(all_teachers, many=True)
#     return APIResponse.respond(data=all_teachers_dump)


@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def regrade_assignment(p, incoming_payload):
    """Re-grade an assignment already graded by a teacher"""
    regrade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    assignment = Assignment.query.get(regrade_assignment_payload.id)
    if assignment.state == AssignmentStateEnum.DRAFT:
        return APIResponse.respond(data="Cannot grade an assignment in Draft state", status=400)

    regraded_assignment = Assignment.mark_grade(
        _id=regrade_assignment_payload.id,
        grade=regrade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    regraded_assignment_dump = AssignmentSchema().dump(regraded_assignment)
    return APIResponse.respond(data=regraded_assignment_dump)
