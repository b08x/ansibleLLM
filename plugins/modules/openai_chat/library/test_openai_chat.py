import unittest
from ansible.module_utils.basic import AnsibleModule
from openai_chat import run_module

class TestOpenAIChatModule(unittest.TestCase):
    def setUp(self):
        self.module = AnsibleModule(
            argument_spec=dict(
                api_key=dict(type='str', required=True, no_log=True),
                model=dict(type='str', required=True),
                messages=dict(type='list', required=True),
                temperature=dict(type='float', default=1),
                max_tokens=dict(type='int', default=None)
            ),
            supports_check_mode=True
        )

    def test_run_module_success(self):
        self.module.params.update(
            api_key='test_api_key',
            model='text-davinci-002',
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': 'Who won the world series in 2020?'}
            ],
            temperature=0.5,
            max_tokens=60
        )
        response = run_module()
        self.assertTrue(response['changed'])
        self.assertIsNotNone(response['message'])

    def test_run_module_failure(self):
        self.module.params.update(
            api_key='invalid_api_key',
            model='text-davinci-002',
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': 'Who won the world series in 2020?'}
            ],
            temperature=0.5,
            max_tokens=60
        )
        with self.assertRaises(Exception):
            run_module()

if __name__ == '__main__':
    unittest.main()
