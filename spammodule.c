#include "python.h" 

static PyObject * 

spam_strcat(PyObject *self, PyObject *args)
{
   char* str1=NULL;
	const char* str2 = NULL;

    if (!PyArg_ParseTuple(args, "ss", &str1,&str2)) // �Ű����� ���� �м��ϰ� ���������� �Ҵ� ��ŵ�ϴ�.
         return NULL; 

	strcat(str1, str2);
    return Py_BuildValue("s", str1);
}

static PyMethodDef SpamMethods[] = {
{"strcat", spam_strcat, METH_VARARGS,
 "Appends a copy of the source string to the destination string."},
 {NULL, NULL, 0, NULL} // �迭�� ���� ��Ÿ���ϴ�.
}; 

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",            // ��� �̸�
    "It is test module.", // ��� ������ ���� �κ�, ����� __doc__�� ����˴ϴ�.
    -1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
