def test_control(accounts, project):
    me = accounts[0]
    control = project.Control.deploy(sender=me)
    tx = control.control(sender=me)
    evt = tx.events[0]
    breakpoint()
