const pushSuccessNotify = (title, message) => {
    new Notify({
      status: 'success',
      title: title,
      text: message,
      effect: 'slide',
      speed: 300,
      customClass: null,
      customIcon: null,
      showIcon: true,
      showCloseButton: true,
      autoclose: true,
      autotimeout: 3000,
      gap: 30,
      distance: 10,
      type: 1,
      position: 'right top'
    })
}

const pushErrorNotify = (title, message) => {
    new Notify({
      status: 'error',
      title: title,
      text: message,
      effect: 'slide',
      speed: 300,
      customClass: null,
      customIcon: null,
      showIcon: true,
      showCloseButton: true,
      autoclose: true,
      autotimeout: 3000,
      gap: 30,
      distance: 10,
      type: 3,
      position: 'right top'
    })
}