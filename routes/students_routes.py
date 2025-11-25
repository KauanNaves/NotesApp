from flask import Blueprint, render_template, request, redirect, url_for
from database.models.notas import Notas

students_routes = Blueprint('students', __name__)

@students_routes.route('/students')
def list_students():
    lista_notas = Notas.select()
    return render_template('students.html', students=lista_notas)


@students_routes.route('/students/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'GET':
        return render_template('add_students.html')
    else:
        name = request.form['name']
        note1 = request.form['note1']
        note2 = request.form['note2']
        note3 = request.form['note3']
        average = (float(note1) + float(note2) + float(note3)) / 3
        average = round(average, 2)
        nova_nota = Notas.create(
            nome = name,
            nota1 = note1,
            nota2 = note2,
            nota3 = note3,
            media = average
        )
        return redirect(url_for('students.list_students'))


@students_routes.route('/students/edit-student/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    if request.method == 'GET':
        student_note = Notas.get_by_id(student_id)
        return render_template('edit_students.html', student=student_note)
    elif request.method == 'POST':
        name = request.form['name']
        note1 = request.form['note1']
        note2 = request.form['note2']
        note3 = request.form['note3']
        average = (float(note1) + float(note2) + float(note3)) / 3
        average = round(average, 2)
        data_student = Notas.get_by_id(student_id)
        data_student.nome = name
        data_student.nota1 = note1
        data_student.nota2 = note2
        data_student.nota3 = note3
        data_student.media = average
        data_student.save()
        return redirect(url_for('students.list_students'))


@students_routes.route('/students/delete-student/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    nota_deletada = Notas.get_by_id(student_id)
    nota_deletada.delete_instance()
    return redirect(url_for('students.list_students'))


